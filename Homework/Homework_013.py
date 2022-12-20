# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random

array = [i / 100 * random.randint(-999,999) for i in range(random.randint(2,10))]

print(array, end=' => ')

for i, element in enumerate(array):
    array[i] = abs(round(element - int(element), 2))

max_element = max(array)
min_element = min(i for i in array if i > 0)

print(max_element - min_element)

