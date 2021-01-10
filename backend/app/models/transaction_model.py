from pydantic import BaseModel
import datetime


class TransactionBase(BaseModel):
    date: datetime.date
    amount: float
    opponent: str
    opponent_account: str
    comment: str
    own_account: str
    category_id: int


class TransactionInDB(TransactionBase):
    id: int

    class Config:
        orm_mode = True
