# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random
random_list = [i * random.randint(-9,9) for i in range(random.randint(1,15))]
print(random_list)

result = sum(element for i, element in enumerate(random_list) if i % 2 != 0)
print(result)
