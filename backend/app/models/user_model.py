from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: Optional[str] = None


class UserInDB(UserBase):
    id: int
    hashed_password:str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str