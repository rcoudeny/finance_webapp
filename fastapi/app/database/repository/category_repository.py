from app.models.category_model import SelfRefCategoryInDB
from sqlalchemy.orm import Session
from fastapi import Depends
import app.database.db_models as models
import app.database.db_schemas as schemas
from app.database.repository.user_repository import get_user_by_email


def get_main_category_from_user_with_email(
    db: Session, user_mail: str
) -> SelfRefCategoryInDB:
    user = get_user_by_email(db, user_mail)

    return (
        db.query(models.Category)
        .filter(
            models.Category.owner_id == user.id
            and models.Category.parent_category_id == None
        )
        .first()
    )


def get_category_with_id(db: Session, user_id: int, category_id: int):
    return (
        db.query(models.Category)
        .filter(
            models.Category.id == category_id and models.Category.owner_id == user_id
        )
        .first()
    )


def add_subcategory_to_parent(
    db: Session, user_mail: str, parent_id: int, name: str
) -> int:
    db_user = get_user_by_email(db, user_mail)
    db_parent_category = get_category_with_id(
        db, db_user.id, parent_id
    )
    if db_parent_category == None:
        return -1
    if db_user.id == db_parent_category.owner_id:
        db_category = models.Category(
            name=name, parent_category_id=parent_id, owner_id=db_user.id
        )

        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category.id
    else:
        return -1


def remove_category(db: Session, user_mail: str, category_id: int):
    db_user = get_user_by_email(db, user_mail)
    db_category = get_category_with_id(db, db_user.id, category_id)
    db.delete(db_category)
    db.commit()


def update_subcategory(
    db: Session,
    user_mail: str,
    category_id: int,
    new_name: str = None,
    new_parent_id: int = None,
):
    db_user = get_user_by_email(db, user_mail)
    db_category = get_category_with_id(db, db_user.id, category_id)
    if new_name != None:
        db_category.name = new_name
    if new_parent_id != None:
        db_category.parent_id = new_parent_id
    db.commit()
    return None
