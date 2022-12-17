# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#     *Пример:*

#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def GetPositiveIntegerValue(message):
    value = input(message)
    while not value.isdigit():
        value = input('Value must be integer. Try again: ')
    return int(value)


def GetFactorial(number):
    factorial = 1
    for i in range(number, 1, -1):
        factorial *= i
    return factorial


user_number = GetPositiveIntegerValue('Enter your number: ')

print(f'If N = {user_number}, then [', end=' ')

for i in range(1, user_number):
    print(GetFactorial(i), end=', ')
print(f'{GetFactorial(user_number)} ]', end=' (')

element = ''
for i in range(1, user_number):
    element = element + '*' + str(i)
    print(element.replace('*', '', 1), end=', ')
print(f'{element}*{user_number}', end='')
print(')')

