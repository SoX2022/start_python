# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random

def HM11():
    random_list = [i * random.randint(-9,9) for i in range(random.randint(1,15))]
    print(random_list, end=' -> elements in odd positions are ')

    for element in random_list[1:len(random_list):2]:
        print(element, end=', ')

    result = sum(element for i, element in enumerate(random_list) if i % 2 != 0)
    print(f"it's sum is: {result}")

def HM25():
    random_list = []
    result = 0

    for i in range (1, 15):
        random_list.append(i * random.randint(-9,9))

    print(random_list, end=' -> elements in odd positions are ')

    for element in random_list[1:len(random_list):2]:
        print(element, end=', ')
        result += element

    print(f"it's sum is: {result}")


def main():
    HM25()

if __name__ == "__main__":
    main()