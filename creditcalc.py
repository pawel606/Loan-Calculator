import math
import argparse
import sys


def monthly_payment(p, n, i):
    a = round(p * i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1)) + 1
    print('Your monthly payment = {}!'.format(a))
    overpayment = a * int(n) - int(p)
    print("Overpayment = {0}".format(overpayment))


def number_of_payments(p, a, i):
    n = math.ceil(math.log((a / (a - i * p)), (1 + i)))
    y = n // 12
    m = n % 12
    if y == 0 and m == 1:
        print('It will take {0} month to repay this loan!'.format(m))
    elif y == 0:
        print('It will take {0} months to repay this loan!'.format(m))
    else:
        print('It will take {0} years and {1} months to repay this loan!'.format(y, m))
    overpayment = n * int(a) - int(p)
    print("Overpayment = {0}".format(overpayment))


def loan_principal(a, i, n):
    p = round(a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)) - 1)
    print('Your loan principal = {0}!'.format(p))
    overpayment = int(a) * int(n) - p
    print("Overpayment = {0}".format(overpayment))


def differentiated_payments(p, i, n):
    all_payments = 0
    for m in range(int(n)):
        differentiated_payment = math.ceil(p / n + i * (p - ((p * (m + 1 - 1)) / n)))
        print("Month {0}: payment is {1}".format(m + 1, differentiated_payment))
        all_payments += differentiated_payment
    overpayment = all_payments - int(p)
    print("\nOverpayment = {0}".format(overpayment))


def check_input_parameters(type, payment, interest, principal, periods):
    if str(type) not in ['annuity', 'diff'] or str(interest) == 'None':
        return False
    elif str(type) == 'diff' and str(payment) != 'None' and len(sys.argv) - 1 != 4:
        return False
    if len(sys.argv) - 1 != 4:
        return False
    if ((str(principal) != 'None' and principal < 0) or
            (str(payment) != 'None' and payment < 0) or
            (str(interest) != 'None' and interest < 0) or
            (str(periods) != 'None' and periods < 0)):
        return False
    return True


parser = argparse.ArgumentParser()
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=float)
parser.add_argument("--interest", type=float)
parser.add_argument("--type")

args = parser.parse_args()
payment = args.payment
principal = args.principal
periods = args.periods
interest = args.interest
type = args.type
correct_input = check_input_parameters(type, payment, interest, principal, periods)
if correct_input:
    interest = interest / (12 * 100)
    if str(type) == 'annuity':
        if str(payment) == 'None':
            monthly_payment(principal, periods, interest)
        elif str(periods) == 'None':
            number_of_payments(principal, payment, interest)
        elif str(principal) == 'None':
            loan_principal(payment, interest, periods)
    elif str(type) == 'diff':
        differentiated_payments(principal, interest, periods)
else:
    print('Incorrect parameters')
