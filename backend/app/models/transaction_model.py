import pandas as pd
from pydantic import BaseModel

class Transaction(BaseModel):#set name of class to call it 
    date: str
    amount: float
    opponent: str
    opponent_account: str
    comment: str
    own_account: str

    def get_date(self):
        return self.date

    def get_amount(self):
        return self.amount

    def get_positiv_expense(self):
        if(amount >= 0):
            return amount
        return 0





