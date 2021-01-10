from app.models.transaction_model import TransactionInDB
from operator import mod
from fastapi import APIRouter, Depends, HTTPException, status
import app.database.repository.transaction_category_repository as category_repo
import app.database.repository.transaction_repository as transaction_repo
import app.database.db_models as models
import app.database.db_schemas as schemas
from sqlalchemy.orm import Session
from app.database.repository.user_repository import get_token


router = APIRouter()


@router.get("/", response_model=schemas.SelfRefTransactionCategoryInDB)
async def get_main_transaction_category(
    token: str = Depends(get_token), db: Session = Depends(models.get_db)
):
    test = category_repo.get_main_transaction_category_from_user_with_email(
        db, token.email
    )
    return test


@router.post("/add-category", response_model=int)
async def add_subcategory_to_parent(
    parent_id: int,
    name: str,
    token: str = Depends(get_token),
    db: Session = Depends(models.get_db),
):
    response: int = category_repo.add_subcategory_to_parent(
        db, token.email, parent_id, name
    )
    if response < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to add subcategory"
        )
    else:
        return response


@router.put("/update-category", response_model=int)
async def update_subcategory(
    category_id: int,
    new_name: str = None,
    new_parent_id: int = None,
    token: str = Depends(get_token),
    db: Session = Depends(models.get_db),
):
    category_repo.update_subcategory(
        db, token.email, category_id, new_name, new_parent_id
    )


# TODO: If category gets removed -> move transactions to main category
@router.delete("/remove-category", response_model=bool)
async def remove_subcategory(
    category_id: int,
    token: str = Depends(get_token),
    db: Session = Depends(models.get_db),
):
    category_repo.remove_category(db, token.email, category_id)


transaction_router = APIRouter()


@transaction_router.get("/", response_model=int)
async def get_main_transaction_category(
    token: str = Depends(get_token), db: Session = Depends(models.get_db)
):

    return category_repo.get_main_transaction_category_from_user_with_email(
        db, token.email
    ).id


@transaction_router.post("/add", response_model=int)
async def add_subcategory_to_parent(
    transaction: schemas.TransactionCreate,
    token: str = Depends(get_token),
    db: Session = Depends(models.get_db),
):
    response: int = transaction_repo.add_transaction(db, token.email, transaction)
    if response < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to add transaction"
        )
    else:
        return response


# TODO: Update transactions
@transaction_router.put("/update", response_model=int)
async def update_transaction(
    category_id: int,
    new_name: str = None,
    new_parent_id: int = None,
    token: str = Depends(get_token),
    db: Session = Depends(models.get_db),
):
    transaction_repo.update_transaction(
        db, token.email, category_id, new_name, new_parent_id
    )


# TODO: Remove transaction
@transaction_router.delete("/delete", response_model=bool)
async def remove_subcategory(
    category_id: int,
    token: str = Depends(get_token),
    db: Session = Depends(models.get_db),
):
    category_repo.remove_category(db, token.email, category_id)