from fastapi import APIRouter
from api.routes import transaction_api

router = APIRouter()
router.include_router(transaction_api.router, tags=["transactions"], prefix="/transactions")