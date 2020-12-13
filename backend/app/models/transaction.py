import pandas as pd
from pydantic import BaseModel

class Transaction(BaseModel):#set name of class to call it 
    date: str
    amount: float
    opponent: str
    opponent_account: str
    comment: str
    own_account: str
    # def __init__(self, date, amount, opponent, opponent_account, comment, own_account):#func set ver
    #     self.date = pd.to_datetime(date, format='%d/%m/%Y')
    #     self.amount = round(amount,2)
    #     self.opponent = opponent
    #     self.opponent_account = opponent_account
    #     self.comment = comment
    #     self.own_account = own_account

    def get_date(self):
        return self.date

    def get_amount(self):
        return self.amount

    def get_positiv_expense(self):
        if(amount >= 0):
            return amount
        return 0





