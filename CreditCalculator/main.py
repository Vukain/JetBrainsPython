import math

principal = int(input("Enter the credit principal:"))

typ = input('''
What do you want to calculate? 
type "m" - for count of months, 
type "p" - for monthly payment:''')

if typ == "p":
    periods = int(input("Enter count of months:"))
    payment = math.ceil(principal / periods)
    if payment * periods != principal:
        last_p = principal-(periods-1)*payment
        print(f"Your monthly payment = {payment} with last month payment = {last_p}.")
    else:
        print(f"Your monthly payment = {payment}")
elif typ == "m":
    payment = int(input("Enter monthly payment:"))
    result = math.ceil(principal / payment)
    if result > 1:
        print(f"It takes {result} months to repay the credit")
    else:
        print(f"It takes 1 month to repay the credit")