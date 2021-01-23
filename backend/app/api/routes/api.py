from fastapi import APIRouter
from app.api.routes import (
    transaction_api,
    authentification_api,
    category_api,
    swagger_token,
)
from app.core.config import API_PREFIX

router: APIRouter = APIRouter()

router.include_router(swagger_token.router, tags=["swagger"])

router.include_router(
    transaction_api.router, tags=["transactions"], prefix=f"{API_PREFIX}/transactions"
)
router.include_router(
    authentification_api.router,
    tags=["authentification"],
    prefix=f"{API_PREFIX}/authentification",
)
router.include_router(
    category_api.router,
    tags=["category"],
    prefix=f"{API_PREFIX}/categorie",
)
router.include_router(
    category_api.transaction_router,
    tags=["transactions"],
    prefix=f"{API_PREFIX}/transactions",
)
