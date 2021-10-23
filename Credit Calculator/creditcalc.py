import math
import sys
import argparse

#   Grabbing arguments from command line
parser = argparse.ArgumentParser()
parser.add_argument("--principal", type=float, help="principal")
parser.add_argument("--interest", type=float, help="interest")
parser.add_argument("--periods", type=int, help="periods")
parser.add_argument("--payment", type=float, help="payment")
parser.add_argument("--type", type=str, help="type")
args = parser.parse_args()

if len(sys.argv) == 4:
    print("Incorrect parameters")

# Calculating Annuity payment
elif args.type == "annuity":
    if (args.payment is not None) and (args.periods is not None) and (args.interest is not None):
        payment = args.payment
        periods = args.periods
        interest = args.interest
        nominal_interest = (interest / 100) / 12
        credit_principal = payment / ((nominal_interest * ((1 + nominal_interest) ** periods)) / (((1 + nominal_interest) ** periods) - 1))
        print("Your credit principal =", str(credit_principal) + "!")
        print("Overpayment =", (payment * periods) - credit_principal)
    elif (args.principal is not None) and (args.payment is not None) and (args.interest is not None):

        nominal_interest = args.interest / (12 * 100)
        period_per_month = math.log((args.payment / (args.payment - nominal_interest * args.principal)), (1 + nominal_interest))
        period_per_month = math.ceil(period_per_month)
        Overpayment = int(args.payment * period_per_month - args.principal)
        numbers_years = period_per_month // 12
        number_month = math.floor(((period_per_month / 12) - numbers_years) * 12)

        if numbers_years > 1 and number_month > 1:
            print(f"You need {numbers_years} years and {number_month} months to repay this credit!")
        elif numbers_years == 1 and number_month == 1:
            print(f"You need {numbers_years} year and {number_month} month to repay this credit!")
        elif numbers_years == 0 and number_month > 1:
            print(f"You need {numbers_years} months to repay this credit!")
        elif numbers_years == 0 and number_month == 1:
            print(f"You need {numbers_years} month to repay this credit!")
        elif number_month == 0 and numbers_years > 1:
            print(f"You need {numbers_years} years to repay this credit!")
        elif number_month == 0 and numbers_years == 1:
            print(f"You need {numbers_years} year to repay this credit!")
        print(f"Overpayment = {Overpayment}")

    elif (args.principal is not None) and (args.periods is not None) and (args.interest is not None):
        principal = args.principal
        periods = args.periods
        interest = args.interest
        nominal_interest = (interest / 100) / 12
        annuity = principal * ((nominal_interest * ((1 + nominal_interest) ** periods)) / (((1 + nominal_interest) ** periods) - 1))
        print("Your annuity payment =", math.ceil(annuity), "!")
        print("Overpayment =", (math.ceil(annuity) * periods) - principal)
    else:
        print("Incorrect parameters")

# Calculating Differentiate payment
elif args.type == "diff":
    if (args.principal is None) or (args.periods is None) or (args.interest is None):
        print("Incorrect parameters")
    else:
        nominal_interest = args.interest / (12 * 100)
        differentiated_payments = []
        for n_periods in range(1, args.periods + 1):
            d = math.ceil(
                (args.principal / args.periods) + nominal_interest * (args.principal - args.principal * (n_periods - 1) / args.periods))
            differentiated_payments.append(d)
            print(f"Month {n_periods}: paid out {d}")
        Overpayment = int(sum(differentiated_payments) - args.principal)
        print()
        print(f"Overpayment = {Overpayment}")

else:
    print("Incorrect parameters")
