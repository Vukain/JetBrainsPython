import math
import sys
import argparse

# A basic credit calculator which main purpose is to work from command line and take several parameters
# It also works when no parameters are given and when launched from main file
# Calculates - count of months, annuity monthly payment, differentiated payments, credit principal


def arg_parser():

    parser = argparse.ArgumentParser(description="Credit Calculator Project")

    parser.add_argument('--type', help="Type of Payment (Annuity or Differential")
    parser.add_argument('--payment', help="Monthly payment", type=int)
    parser.add_argument('--principal', help="Credit principal", type=int)
    parser.add_argument('--periods', help="Count of months", type=int)
    parser.add_argument('--interest', help="Credit interest (rate of interest)", type=float)

    return parser.parse_args()


def calc_periods():

    try:
        _periods = math.ceil(math.log(monthly_payment
                                      / (monthly_payment - nominal_interest * principal), 1 + nominal_interest))
        years = _periods // 12
        months = _periods % 12

        plural_year = "years" if years > 1 else "year"
        plural_month = "months" if months > 1 else "month"
        summed_payments = _periods * monthly_payment

        if years and months:
            print(f"You need {years} {plural_year} and {months} {plural_month} to repay this credit!")
        elif years:
            print(f"You need {years} {plural_year} to repay this credit!")
        else:
            print(f"You need {months} {plural_month} to repay this credit!")

        print(f"\nOverpayment = {summed_payments - principal}")
    except ValueError:
        print("You will never repay it!!!")
    except Exception:
        print("I'm lost")


def calc_annuity_payment():

    _monthly_payment = math.ceil(principal * ((nominal_interest * math.pow(1 + nominal_interest, periods))
                                 / (math.pow(1 + nominal_interest, periods) - 1)))
    summed_payments = periods * _monthly_payment

    print(f"Your annuity payment = {math.ceil(_monthly_payment)}!")
    print(f"\nOverpayment = {summed_payments - principal}")


def calc_differ_payment():

    summed_payments = 0
    month = 1

    for _p in range(periods):
        dif_payment = math.ceil((principal / periods) + nominal_interest
                                * (principal - ((principal * (month - 1)) / periods)))
        print(f"Month {month}: paid out {dif_payment}")
        summed_payments += dif_payment
        month += 1

    print(f"\nOverpayment = {summed_payments - principal}")


def calc_principal():

    _principal = math.ceil(monthly_payment / ((nominal_interest * math.pow(1 + nominal_interest, periods))
                                              / (math.pow(1 + nominal_interest, periods) - 1)))
    summed_payments = periods * monthly_payment

    print(f"Your credit principal = {_principal}!")
    print(f"\nOverpayment = {summed_payments - _principal}")


# launching from cmd with no parameters of from within a file
if len(sys.argv) == 1 or "__name__" == "__main__":
    
    typ = input('''
    What do you want to calculate?
    type "n" - for count of months,
    type "a" - for annuity monthly payment,
    type "d" - for differentiated payments,
    type "p" - for credit principal: ''')

    interest = float(input("Enter credit interest: "))
    nominal_interest = (interest / (12 * 100))

    if typ == "n":
        principal = int(input("Enter credit principal: "))
        monthly_payment = int(input("Enter monthly payment: "))
        calc_periods()
    elif typ == "a":
        principal = int(input("Enter credit principal: "))
        periods = int(input("Enter count of periods: "))
        calc_annuity_payment()
    elif typ == "d":
        principal = int(input("Enter credit principal: "))
        periods = int(input("Enter count of periods: "))
        calc_differ_payment()
    elif typ == "p":
        monthly_payment = int(input("Enter monthly payment: "))
        periods = int(input("Enter count of periods: "))
        calc_principal()
    else:
        print("Incorrect Type")
# launching with parameters
else:
    args = arg_parser()

    if args.interest and len(sys.argv) == 5:
        interest = args.interest
        nominal_interest = (interest / (12 * 100))
        if args.type == "diff" and not args.payment:
            principal = args.principal
            periods = args.periods
            calc_differ_payment()
        elif args.type == "annuity" and all([args.periods, args.principal]):
            principal = args.principal
            periods = args.periods
            calc_annuity_payment()
        elif args.type == "annuity" and all([args.payment, args.principal]):
            principal = args.principal
            monthly_payment = args.payment
            calc_periods()
        elif args.type == "annuity" and all([args.payment, args.periods]):
            monthly_payment = args.payment
            periods = args.periods
            calc_principal()
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
