# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


def main():
    user_array = []
    result_array = []
    user_array = list(map(int, input('Enter sequence of integer numbers. Use space bar to split. ').split()))

    for element in user_array:
        if user_array.count(element) == 1:
            result_array.append(element)
    print(f'Unique elements in array {user_array} are - ', end='')
    print(result_array)


if __name__ == "__main__":
    main()

