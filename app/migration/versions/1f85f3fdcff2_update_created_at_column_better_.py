"""update created_at column, better documention

Revision ID: 1f85f3fdcff2
Revises: 1795a9c2b0c7
Create Date: 2025-05-20 21:11:31.182873

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f85f3fdcff2'
down_revision: Union[str, None] = '1795a9c2b0c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
