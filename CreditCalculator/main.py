import math
import sys

if len(sys.argv) < 2:
    # For non cmd operations - start without parameters
    typ = input('''
    What do you want to calculate?
    type "n" - for count of months,
    type "a" - for annuity monthly payment,
    type "d" - for differentiated payments,
    type "p" - for credit principal: ''')
    if typ == "n":
        principal = int(input("Enter credit principal: "))
        monthly_payment = float(input("Enter monthly payment: "))
        interest = float(input("Enter credit interest: "))
    elif typ in ["d", "a"]:
        principal = int(input("Enter credit principal: "))
        periods = int(input("Enter count of periods: "))
        interest = float(input("Enter credit interest: "))
    elif typ == "p":
        monthly_payment = float(input("Enter monthly payment: "))
        periods = int(input("Enter count of periods: "))
        interest = float(input("Enter credit interest: "))
elif sys.argv[1] == "diff":
    typ = "d"
    principal = int(input("Enter credit principal: "))
    periods = int(input("Enter count of periods: "))
    interest = float(input("Enter credit interest: "))
    
principal = int(input("Enter credit principal: "))
monthly_payment = float(input("Enter monthly payment: "))
periods = int(input("Enter count of periods: "))
interest = float(input("Enter credit interest: "))


nominal_interest = (interest / (12 * 100))

if typ == "n":
    # principal = int(input("Enter credit principal: "))
    # monthly_payment = float(input("Enter monthly payment: "))
    # interest = float(input("Enter credit interest: "))

    periods = math.ceil(math.log(monthly_payment
                                 / (monthly_payment - nominal_interest * principal), 1 + nominal_interest))
    years = periods // 12
    months = periods % 12

    plural_year = "years" if years > 1 else "year"
    plural_month = "months" if years > 1 else "month"
    summed_payments = periods * monthly_payment

    if years and months:
        print(f"You need {years} {plural_year} and {months} {plural_month} to repay this credit!")
    elif years:
        print(f"You need {years} {plural_year} to repay this credit!")
    else:
        print(f"You need {months} {plural_month} to repay this credit!")

    print(f"\nOverpayment = {summed_payments - principal}")

elif typ == "d":
    summed_payments = 0
    month = 1
    for _p in range(periods):
        dif_payment = math.ceil((principal / periods) + nominal_interest
                                * (principal - ((principal * (month - 1)) / periods)))
        print(f"Month {month}: paid out {dif_payment}")
        summed_payments += dif_payment
        month += 1

    print(f"Overpayment = {summed_payments - principal}")
    print(f"\nOverpayment = {summed_payments - principal}")

elif typ == "a":
    # principal = int(input("Enter credit principal: "))
    # periods = int(input("Enter count of periods: "))
    # interest = float(input("Enter credit interest: "))

    monthly_payment = principal * ((nominal_interest * math.pow(1 + nominal_interest, periods))
                                   / (math.pow(1 + nominal_interest, periods) - 1))

    summed_payments = periods * monthly_payment

    print(f"Your annuity payment = {math.ceil(monthly_payment)}!")
    print(f"\nOverpayment = {summed_payments - principal}")

elif typ == "p":
    # monthly_payment = float(input("Enter monthly payment: "))
    # periods = int(input("Enter count of periods: "))
    # interest = float(input("Enter credit interest: "))

    principal = monthly_payment / ((nominal_interest * math.pow(1 + nominal_interest, periods))
                                   / (math.pow(1 + nominal_interest, periods) - 1))
    summed_payments = periods * monthly_payment

    print(f"Your credit principal = {principal}!")
    print(f"\nOverpayment = {summed_payments - principal}")

