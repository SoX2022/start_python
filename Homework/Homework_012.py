# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


import random
#import math

array = [i * random.randint(-9,9) for i in range(random.randint(1,10))]
result = []

#for i in range(ceil(len(array) / 2)):
for i in range(round(len(array) / 2 + 0.1)):
    result.append(array[i] * array[-i -1])
print(f'{array} => {result}')

