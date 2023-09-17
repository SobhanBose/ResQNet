from fastapi import APIRouter
from app.config import *

router = APIRouter()

@router.get("/")
def home():
    return {"status": 1}