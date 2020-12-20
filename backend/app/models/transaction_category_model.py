from typing import List, Optional
from app.models.transaction_model import Transaction
from pydantic import BaseModel


class TransactionCategoryBase(BaseModel):
    id: int
    name: str
    parent_category_id: int

    # def get_all_transactions(self):
    #     total = 0
    #     for subcategory in self.subcategories:
    #         total += subcategory.getAllTransactions()
    #     for transaction in self.transactions:
    #         total += transaction.getAmount()
    #     return round(total,2)

    # def add_transaction(self, transaction):
    #     self.transactions.append(transaction)

    # def add_subcategory(self, category):
    #     self.subcategories.append(category)

    # def find_subcategory_with_name(self, name: str):
    #     for cat in self.subcategories:
    #         if (cat.name == name):
    #             return cat
    #     return None
