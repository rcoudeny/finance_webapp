from app.models.user_model import UserBase, UserDTO, UserInDB
from app.models.category_model import SelfRefCategoryInDB
from app.models.transaction_model import TransactionBase, TransactionInDB


class UserCreate(UserBase):
    password: str


class UserInDB(UserInDB):
    pass


class UserTest(UserDTO):
    pass


class SelfRefCategoryInDB(SelfRefCategoryInDB):
    pass


class TransactionCreate(TransactionBase):
    class Config:
        orm_mode = True
