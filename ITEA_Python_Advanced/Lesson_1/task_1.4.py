# Реализовать функцию bank, которая приннимает
# следующие аргументы: сумма депозита, кол-во лет,
# и процент. Результатом выполнения должна быть
# сумма по истечению депозита
user_deposit = int(input('Enter your deposit'))
user_percent = float(input('Enter your percent'))
user_deposit_term = float(input('Enter your deposit term'))


def bank(sum_of_deposit, years, percent):

    num_of_days_on_deposit = years * 365
    final_sum = sum_of_deposit + sum_of_deposit * percent * num_of_days_on_deposit / 365 / 100

    return print('Your deposit amount', final_sum)


bank(user_deposit, user_deposit_term, user_percent)
