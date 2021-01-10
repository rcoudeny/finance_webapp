from app.models.user_model import UserBase, UserDTO, UserInDB
from app.models.transaction_category_model import SelfRefTransactionCategoryInDB
from app.models.transaction_model import TransactionBase, TransactionInDB


class UserCreate(UserBase):
    password: str


class UserInDB(UserInDB):
    pass


class UserTest(UserDTO):
    pass


class SelfRefTransactionCategoryInDB(SelfRefTransactionCategoryInDB):
    pass


class TransactionCreate(TransactionBase):
    class Config:
        orm_mode = True
