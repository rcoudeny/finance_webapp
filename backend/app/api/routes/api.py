from fastapi import APIRouter
from app.api.routes import transaction_api, authentification_api
from app.core.config import API_PREFIX

router = APIRouter()
router.include_router(transaction_api.router, tags=["transactions"], prefix=f"{API_PREFIX}/transactions")
router.include_router(authentification_api.router, tags=["authentification"])
# router.include_router(test_api.router, tags=["extra_auth"], prefix="/testlogin")
