from operator import mod
from fastapi import APIRouter, Depends, HTTPException, status
import app.database.repository.transaction_category_repository as cat_repo
import app.database.db_models as models
import app.database.db_schemas as schemas
from sqlalchemy.orm import Session
from app.database.repository.user_repository import get_token


router = APIRouter()


@router.get("/")
async def get_main_transaction_category(
    token: str = Depends(get_token), db: Session = Depends(models.get_db)
):
    return cat_repo.get_main_transaction_category_from_user_with_email(db, token.email)


@router.get("/add-subcategory", response_model=int)
async def add_subcategory_to_parent(
    parent_id: int,
    name: str,
    token: str = Depends(get_token),
    db: Session = Depends(models.get_db),
):
    response: int = cat_repo.add_subcategory_to_parent(db, token.email, parent_id, name)
    if response < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to add subcategory"
        )
    else:
        return response
