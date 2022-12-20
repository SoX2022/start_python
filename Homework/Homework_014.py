# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


import random

user_number = random.randint(-100, 100)
new_user_number = str(bin(user_number)).replace('0b', '')
if new_user_number[0] == '-':
    new_user_number = '1' + new_user_number.replace('-','')
print(f'{user_number} -> {new_user_number}')

