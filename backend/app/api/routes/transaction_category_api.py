from fastapi import APIRouter, Depends
import app.database.repository.transaction_category_repository as cat_repo
import app.database.db_models as models
import app.database.db_schemas as schemas
from sqlalchemy.orm import Session
from app.database.repository.user_repository import get_token


router = APIRouter()

@router.get("/")
async def get_main_transaction_category(token: str = Depends(get_token), db: Session = Depends(models.get_db)):
    cat_repo.get_main_transaction_category_from_user_with_email(db, token.email)