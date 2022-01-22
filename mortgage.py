from prettytable import PrettyTable
import math

details = []


def get_customer_data(n):
    current_duration = '  '
    new_duration = ' '
    interest_paid = 0
    new_interest = 0
    savings = 0
    fees = ' '
    i = 1
    currency = ' '
    while i <= n:
        # input values
        # name
        name = input('Enter name of borrower : ')
        # mortgagee balance
        mortgage_balance = float(input('Enter the mortgage balance : $'))
        # interest
        interest = float(input('Enter annual interest Rate : '))
        # monthly payment
        current_monthly_payment = float( input('Enter current monthly payment : $'))
        # new monthly payment
        extra_monthly_payment = float(input('Enter extra monthly payment : $'))
        extra_monthly_payment = extra_monthly_payment + current_monthly_payment
        # **************************************************************
        current_duration_months = calculate_duration(current_monthly_payment, interest, mortgage_balance)
        years = int(current_duration_months / 12)
        months = int(current_duration_months % 12)
        current_duration = str(years) + 'yrs' + ' ' + str(months) + 'mo'
        # ****************************************************************
        current_interest = round(((current_monthly_payment * current_duration_months) - mortgage_balance), 2)

        new_duration_months =  calculate_duration(extra_monthly_payment, interest, mortgage_balance)
        years = int(new_duration_months / 12)
        months = int(new_duration_months % 12)
        new_duration = str(years) + 'yrs' + ' ' + str(months) + 'mo'

        new_interest = round(((extra_monthly_payment * new_duration_months) - mortgage_balance), 2)
        savings = round( current_interest - new_interest,2)
        # convert  to string to concatenate  currency
        currency = '$'
        savings = currency + str(savings)
        interest = str(format(interest,".3f")) + '%'
        current_interest = currency + str(current_interest)
        new_interest = currency + str(new_interest)
        mortgage_balance = currency + str(mortgage_balance)
        current_monthly_payment = currency + str(current_monthly_payment)
        extra_monthly_payment = currency + str(extra_monthly_payment)

        if new_duration_months <= (current_duration_months / 2):
            fees = 'Extra Fees'
        else:
            fees = 'No Fee'

        record = [name,
                  mortgage_balance,
                  interest,
                  current_monthly_payment,
                  current_duration,
                  current_interest,
                  extra_monthly_payment,
                  new_duration,
                  new_interest,
                  savings,
                  fees
                  ]
        details.append(record)
        print()
        i += 1

def calculate_duration(current_monthly_payment, interest, mortgage_balance):
    duration = 0.0
    try:
        pmt = current_monthly_payment
        i = ((interest / 100) / 12)
        pv = mortgage_balance
        constant = (pmt / i)
        numerator = (constant / (constant - pv))
        denominator = (1 + i)
        duration = math.log10(numerator) / math.log10(denominator)
    except ValueError:
        print('Error Calculating log')

    return round(duration)


def print_list(details):
    t = PrettyTable()
    t.field_names = ["Name", "Mortgage Balance", "Interest Rate", "Payment", "Current Duration", "Interest",
                     "New Payment", "New Duration", "New Interest", "Savings", "Fees"]
    t.add_rows(details)
    print(t)

if __name__ == '__main__':

    get_customer_data(int(input('Enter the  number of entries to  calculate mortgage : ')))
    details  = sorted(details,reverse =  True , key=lambda x: float((x[9][1:])))
    print_list(details)

