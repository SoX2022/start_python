# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def GetPositiveIntegerValue(message):
    value = input(message)
    while not value.isdigit():
        value = input('Value must be integer. Try again: ')
    return int(value)


user_number = GetPositiveIntegerValue('Enter the number for Fibanachi: ')
fibanachi = [0]

if user_number == 0:
    print('[0]')
else:
    fibanachi = [1, 0, 1]
    for i in range(2, user_number + 1):
        fibanachi.append(fibanachi[len(fibanachi) - 1] + fibanachi[len(fibanachi) - 2])
        fibanachi.insert(0, fibanachi[len(fibanachi) - 1] * (-1) ** (i - 1))

print(f'For k = {user_number} list is {fibanachi}')

