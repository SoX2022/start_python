# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random

def HM13():
    array = [i / 100 * random.randint(-999, 999) for i in range(random.randint(2, 10))]

    print(array, end=' => ')

    for i, element in enumerate(array):
        array[i] = abs(round(element - int(element), 2))

    max_element = max(array)
    min_element = min(i for i in array if i > 0)

    print(max_element - min_element)

def HM25():
    array = []

    for i in range(random.randint(2, 10)):
        array.append(i / 100 * random.randint(-999, 999))

    print(array, end=' => ')

    for i in range(len(array)):
        array[i] = abs(round(array[i] - int(array[i]), 2))

    max_element = max(array)
    min_element = min(i for i in array if i > 0)

    print(max_element - min_element)


def main():
    HM25()


if __name__ == "__main__":
    main()
