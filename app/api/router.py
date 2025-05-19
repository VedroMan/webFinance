
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

from app.api.schemas import (
    WalletModel,
    UserModel,
    IncomeTransactionModel,
    ExpenseTransactionModel
)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

# MARK: API




# MARK: Views

def template_response(request: Request):
    return templates.TemplateResponse("index.html", { "request": request})

@router.get("/")
def home_view(request: Request):
    return template_response(request)
    
@router.get("/balance")
def balance_view(request: Request):
    return template_response(request)

@router.get("/budget")
def budget_view(request: Request):
    return template_response(request)

@router.get("/analytics")
def analytics_view(request: Request):
    return template_response(request)

@router.get("/settings")
def settings_view(request: Request):
    return template_response(request)