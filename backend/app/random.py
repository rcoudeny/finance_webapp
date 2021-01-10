# import math
# import datetime

# leeftijd = 27
# maandloon = 1920
# kosten = 920
# remaining = 0
# budget = 0
# amount = maandloon-kosten-remaining
# roi = 7


# birthday = 1998
# total = 0
# future = leeftijd + birthday

# months = (future - datetime.datetime.now().year)*12


# monthly_roi = math.pow(((roi/100)+1),(1/12))
# monthly_rev = 0

# for i in range(1, months+1):
#     old_total = total
#     total = total * monthly_roi + amount
#     monthly_rev = total - old_total - amount
#     budget = budget + maandloon - kosten - amount
#     if(monthly_rev>10000 or total>1000000):
#         months = i
#         break





# print(str(months/12) + " With a monthly rev at the end of " + str(format(monthly_rev,".2f")))
# print()
# print("Totale inbreng:\t" + format(amount*months,".2f"))
# print("Winst:\t\t" + format(total-amount*months,".2f"))
# print("Totaal budget:\t" + format(total,".2f"))
# print()
# print("Gespaard:\t" + format(budget,".2f"))

import pandas as pd

df = pd.read_excel(
        "/Users/robbe/Documents/Projects/finance_webapp/assets/searchMovement.xls"
    )
df.fillna("")
   # main_category = TransactionCategoryBase(name="Main")
opponents = set()

for row in df.iterrows():
    print(row)
        # temp_transaction = Transaction(
        #     date="/".join(row[1][0].split("/")[::-1]),
        #     amount=row[1][1],
        #     opponent=str(row[1][3]),
        #     opponent_account=str(row[1][4]),
        #     comment=str(row[1][6]),
        #     own_account=str(row[1][7]),
        # )
        # if temp_transaction.opponent in opponents:
        #     main_category.find_subcategory_with_name(
        #         temp_transaction.opponent
        #     ).add_transaction(temp_transaction)
        # else:
        #     opponents.add(temp_transaction.opponent)
        #     new_category = TransactionCategoryBase(name=temp_transaction.opponent)
        #     main_category.add_subcategory(new_category)
        #     new_category.add_transaction(temp_transaction)