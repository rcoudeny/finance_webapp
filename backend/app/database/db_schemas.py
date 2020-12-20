from app.models.user_model import UserBase
from app.models.transaction_category_model import TransactionCategoryBase


class UserCreate(UserBase):
    password: str


class TransactionCategory(TransactionCategoryBase):
    pass