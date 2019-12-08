user_deposit = int(input('Enter your deposit'))
user_percent = float(input('Enter your percent'))
user_deposit_term = float(input('Enter your deposit term'))


def bank(deposit_sum, number_of_years, percent):

    number_of_days_on_deposit = number_of_years * 365
    final_sum = deposit_sum + deposit_sum * percent * number_of_days_on_deposit / 365 / 100

    return print('Your deposit amount', final_sum)


bank(user_deposit, user_deposit_term, user_percent)