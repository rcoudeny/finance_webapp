from app.database.db_models import Transaction
from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: Optional[str] = None


class UserDTO(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserInDB(UserDTO):
    hashed_password: str

    class Config:
        orm_mode = True


class AuthorizedUser(UserBase):
    token: str