from app.models.user_model import UserDTO
from typing import List, Optional
from app.models.transaction_model import TransactionInDB
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    owner: Optional[UserDTO]

    # parent_category: Optional[]


class SelfRefCategoryInDB(BaseModel):
    id: int
    name: str
    # owner: Optional[UserDTO]
    sub_categories: Optional[List["SelfRefCategoryInDB"]]
    transactions: Optional[List[TransactionInDB]]

    class Config:
        orm_mode = True


SelfRefCategoryInDB.update_forward_refs()
