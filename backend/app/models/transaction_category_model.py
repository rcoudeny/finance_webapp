from app.models.user_model import UserDTO
from typing import List, Optional
from app.models.transaction_model import TransactionInDB
from pydantic import BaseModel


class TransactionCategoryBase(BaseModel):
    name: str
    owner: Optional[UserDTO]

    # parent_category: Optional[]


class SelfRefTransactionCategoryInDB(BaseModel):
    id: int
    name: str
    # owner: Optional[UserDTO]
    sub_categories: Optional[List["SelfRefTransactionCategoryInDB"]]
    transactions: Optional[List[TransactionInDB]]

    class Config:
        orm_mode = True


SelfRefTransactionCategoryInDB.update_forward_refs()
