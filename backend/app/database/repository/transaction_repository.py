from sqlalchemy.orm import Session
import app.database.db_models as models
import app.database.db_schemas as schemas
from app.database.repository.category_repository import (
    get_main_category_from_user_with_email,
    get_category_with_id,
)


def add_transaction(
    db: Session, user_mail: str, transaction: schemas.TransactionCreate
) -> int:
    category = transaction.category_id
    if category == 0:
        category = get_main_category_from_user_with_email(db, user_mail)
    else:
        category = get_category_with_id(db, 1, category)
    db_transaction = models.Transaction(
        date=transaction.date,
        amount=transaction.amount,
        opponent=transaction.opponent,
        opponent_account=transaction.opponent_account,
        comment=transaction.comment,
        own_account=transaction.own_account,
        category=category,
    )

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction.id
