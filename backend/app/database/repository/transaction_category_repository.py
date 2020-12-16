from sqlalchemy.orm import Session
from fastapi import Depends
import app.database.db_models as models
import app.database.db_schemas as schemas
from app.database.repository.user_repository import get_user_by_email

def get_main_transaction_category_from_user_with_email(db : Session, user_mail: str):
    user = get_user_by_email(db, user_mail)
    return db.query(models.TransactionCategory).filter(models.TransactionCategory.id == user.main_transaction_category_id).first()