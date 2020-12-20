from sqlalchemy.orm import Session
from fastapi import Depends
import app.database.db_models as models
import app.database.db_schemas as schemas
from app.database.repository.user_repository import get_user_by_email


def get_main_transaction_category_from_user_with_email(db: Session, user_mail: str):
    user = get_user_by_email(db, user_mail)

    # TODO dit werkt nog niet met de geupdate dingen
    return (
        db.query(models.TransactionCategory)
        .filter(
            models.TransactionCategory.owner_id == user.id
            and models.TransactionCategory.parent_category_id == None
        )
        .first()
    )


def get_transaction_category_with_id(db: Session, category_id: int):
    return (
        db.query(models.TransactionCategory)
        .filter(models.TransactionCategory.id == category_id)
        .first()
    )


def add_subcategory_to_parent(db: Session, user_mail, parent_id: int, name: str):
    db_user = get_user_by_email(db, user_mail)
    db_parent_transaction_category = get_transaction_category_with_id(db, parent_id)
    if db_user.id == db_parent_transaction_category.owner_id:
        db_transaction_category = models.TransactionCategory(
            name=name, parent_category_id=parent_id, owner_id=db_user.id
        )

        db.add(db_transaction_category)
        db.commit()
        db.refresh(db_transaction_category)
        return db_transaction_category.id
    else:
        return -1