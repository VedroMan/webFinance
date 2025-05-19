
from typing import TypeVar, Generic
from pydantic import BaseModel

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete, func
from sqlalchemy.ext.asyncio import AsyncSession

from database import Base

from loguru import logger

T = TypeVar('T', bound=Base)


class BaseDAO(Generic[T]):
    model: type[T]
    
    def __init__(self, session: AsyncSession):
        self._session = session
        if self.model is None:
            raise ValueError("Модель должна быть указана в дочернем классе")
        
    
    # MARK: CRUD
    
    async def create(self, values: BaseModel):
        values_dict = values.model_dump(exclude_unset=True)
        logger.info(f"Создание записи {self.model.__name__} с параметрами: {values_dict}")
        try:
            new_instance = self.model(**values_dict)
            self._session.add(new_instance)
            logger.info(f"Запись {self.model.__name__} успешно добавлена")
            await self._session.flush()
            return new_instance
        
        except SQLAlchemyError as e:
            logger.info(f"Ошибка при создании записи: {e}")
            raise
        
    
    async def read(self, filters: BaseModel | None = None):
        filters_dict = filters.model_dump(exclude_unset=True) if filters else {}
        logger.info(f"Поиск всех записей {self.model.__name__} по фильтрам: {filters_dict}")
        try:
            query = select(self.model).filter_by(**filters_dict) # построение sql запроса с применением фильтров
            result = await self._session.execute(query)
            records = result.scalars().all()
            logger.info(f"Найдено {len(records)} записей")
            return records
        
        except SQLAlchemyError as e:
            logger.info(f"Ошибка при поиске всех записей по фильтрам {filters_dict}: {e}")
            raise
    
    
    async def update(self, filters: BaseModel, values: BaseModel):
        filters_dict = filters.model_dump(exclude_unset=True)
        values_dict = values.model_dump(exclude_unset=True)
        logger.info(f"Обновление записей {self.model.__name__} по фильтрам: {filters_dict} с параметрами: {values_dict}")
        try:
            query = (
                sqlalchemy_update(self.model)
                .where(*[getattr(self.model, k) == v for k, v in filters_dict.items()])
                .values(**values_dict)
                .execution_options(synchronize_session="fetch")
                
            )
            result = await self._session.execute(query)
            logger.info(f"Обновлено {result.rowcount} записей")
            await self._session.flush()
            return result.rowcount
        
        except SQLAlchemyError as e:
            logger.info(f"Ошибка при обновлении записей: {e}")
            raise
    
    
    async def delete(self, filters: BaseModel):
        filters_dict = filters.model_dump(exclude_unset=True)
        logger.info(f"Удаление записей {self.model.__name__} по фильтрам: {filters_dict}")
        if not filters_dict:
            logger.error("Нужен хотя бы один фильтр для удаления")
            raise ValueError("Нужен хотя бы один фильтр для удаления")
        try:
            query = sqlalchemy_delete(self.model).filter_by(**filters_dict)
            result = await self._session.execute(query)
            logger.info(f"Удалено {result.rowcount} записей")
            await self._session.flush()
            return result.rowcount
        
        except SQLAlchemyError as e:
            logger.info(f"Ошибка при удалении записей: {e}")
            raise
    
    
    # MARK: Фильтры
    
    
    async def find_one_or_none_by_id(self, data_id: int):
        try:
            query = select(self.model).filter_by(id=data_id)
            result = await self._session.execute(query)
            record = result.scalar_one_or_none()
            log_message = f"Запись {self.model.__name__} с ID {data_id} {'найдена' if record else 'не найдена'}."
            logger.info(log_message)
            return record
        
        except SQLAlchemyError as e:
            logger.info(f"Ошибка при поиске записи с ID {data_id}: {e}")
            raise
        
        
    async def find_one_or_none_by_filters(self, filters: BaseModel):
        filters_dict = filters.model_dump(exclude_unset=True)
        logger.info(f"Поиск одной записи {self.model.__name__} по фильтрам: {filters_dict}")
        try:
            query = select(self.model).filter_by(**filters_dict)
            result = await self._session.execute(query)
            record = result.scalar_one_or_none()
            log_message = f"Запись {'найдена' if record else 'не найдена'} по фильтрам: {filters_dict}"
            logger.info(log_message)
            return record
        
        except SQLAlchemyError as e:
            logger.info(f"Ошибка при поиске записи по фильтрам {filters_dict}: {e}")
            raise
        
    
    # count и доп фильтрации, потом придумаю
    async def count(self, filters: BaseModel | None = None):
        filters_dict = filters.model_dump(exclude_unset=True) if filters else {}
        logger.info(f"Подсчёт количества записей {self.model.__name__} по фильтрам: {filters_dict}")
        try:
            query = select(self.model).filter_by(**filters_dict)
            result = await self._session.execute(query)
            
        except SQLAlchemyError as e:
            #
            raise