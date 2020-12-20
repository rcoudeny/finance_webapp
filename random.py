import math
import datetime

leeftijd = 65
maandloon = 2700
kosten = 700
remaining = 0
budget = 0
amount = maandloon-kosten-remaining
roi = 7


birthday = 1998
total = 0
future = leeftijd + birthday

months = (future - datetime.datetime.now().year)*12


monthly_roi = math.pow(((roi/100)+1),(1/12))
monthly_rev = 0

for i in range(1, months+1):
    old_total = total
    total = total * monthly_roi + amount
    monthly_rev = total - old_total - amount
    budget = budget + maandloon - kosten - amount




print(str(months/12) + " With a monthly rev at the end of " + str(format(monthly_rev,".2f")))
print()
print("Totale inbreng:\t" + format(amount*months,".2f"))
print("Winst:\t\t" + format(total-amount*months,".2f"))
print("Totaal budget:\t" + format(total,".2f"))
print()
print("Gespaard:\t" + format(budget,".2f"))