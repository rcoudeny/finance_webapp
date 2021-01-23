from fastapi import APIRouter
from typing import Optional
import pandas as pd
from fastapi import File, UploadFile
import csv, re
from app.models.transaction_model import TransactionBase
from app.models.category_model import CategoryBase

router = APIRouter()

# TODO: Dit wordt niet gebruikt omdat de transactions in category zitten
# TODO: Data initaliseren met excel bestandje (Doen via flutter?)
# @router.post("/upload")
# async def upload_transactions_with_excel(
#     file: UploadFile = File(...),
# ) -> CategoryBase:
#     data = file.file
#     df = pd.read_excel(data)
#     df.fillna("")
#     main_category = CategoryBase(name="Main")

#     for row in df.iterrows():

#         temp_transaction = Transaction(
#             date="/".join(row[1][0].split("/")[::-1]),
#             amount=row[1][1],
#             opponent=str(row[1][3]),
#             opponent_account=str(row[1][4]),
#             comment=str(row[1][6]),
#             own_account=str(row[1][7]),
#         )
#         print()
#         main_category.add_transaction(temp_transaction)
#     return main_category


# @router.get("/upload_from_file")
# async def fake_upload_file() -> CategoryBase:
#     # file: UploadFile = File(...) Dit in bovenstaande steken als ik er iets mee wil doen
#     # data = file.file
#     df = pd.read_excel(
#         "/Users/robbe/Documents/Projects/finance_webapp/assets/searchMovement.xls"
#     )
#     df.fillna("")
#     main_category = CategoryBase(name="Main")
#     opponents = set()

#     for row in df.iterrows():
#         temp_transaction = Transaction(
#             date="/".join(row[1][0].split("/")[::-1]),
#             amount=row[1][1],
#             opponent=str(row[1][3]),
#             opponent_account=str(row[1][4]),
#             comment=str(row[1][6]),
#             own_account=str(row[1][7]),
#         )
#         if temp_transaction.opponent in opponents:
#             main_category.find_subcategory_with_name(
#                 temp_transaction.opponent
#             ).add_transaction(temp_transaction)
#         else:
#             opponents.add(temp_transaction.opponent)
#             new_category = CategoryBase(name=temp_transaction.opponent)
#             main_category.add_subcategory(new_category)
#             new_category.add_transaction(temp_transaction)

#     # sub_category = ExpenseCategory(category_name = "DRINKGELD")
#     # eigen_category = ExpenseCategory(category_name = "Eigen rekening")
#     # main_category.addSubCategory(sub_category)
#     # main_category.addSubCategory(eigen_category)

#     # for row in df.iterrows():

#     #     tempexpense = Expense(
#     #             date = "/".join(row[1][0].split("/")[::-1]),
#     #             amount = row[1][1],
#     #             opponent = str(row[1][3]),
#     #             opponent_account = str(row[1][4]),
#     #             comment = str(row[1][6]),
#     #             own_account = str(row[1][7]))
#     #     print()
#     #     if(tempexpense.comment == "DRINKGELD"):
#     #         sub_category.addExpense(tempexpense)
#     #     elif(tempexpense.opponent_account == "BE03 0634 9683 8984"):
#     #         eigen_category.addExpense(tempexpense)
#     #     else:
#     #         main_category.addExpense(tempexpense)

#     return main_category