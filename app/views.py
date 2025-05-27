
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


def template_response(request: Request):
    return templates.TemplateResponse("index.html", { "request": request })

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