# Задайте список из n чисел последовательности (1 + 1 / n)^n и выведите на экран их сумму.
    
#     *Пример:*
    
#     - Для n=4 [2, 2.25, 2.37, 2.44]
#     Сумма 9.06


def GetPositiveIntegerValue(message):
    value = input(message)
    while not value.isdigit():
        value = input('Value must be integer. Try again: ')
    return int(value)

def HM8():
    user_number = GetPositiveIntegerValue('Enter your number: ')
    print(f'For n={user_number} ', end='[')

    for i in range(1, user_number):
        print(round((1 + 1 / i) ** i, 2), end=', ')
    print(f'{round((1 + 1 / user_number) ** user_number, 2)}]')

def HM25():
    user_number = GetPositiveIntegerValue('Enter your number: ')
    print(f'For n={user_number} ', end='')
    result = [round((1 + 1 / i) ** i, 2) for i in range(1, user_number + 1)]
    print(result)


def main():
    HM25()


if __name__ == "__main__":
    main()