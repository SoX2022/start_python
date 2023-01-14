# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def GetMaxCoefficient(max_coefficient, array):
    for i, element in enumerate(array):
        if int(array[i][element.find('^') + 1]) > max_coefficient and int(element.find('^')) != -1:
            max_coefficient = int(array[i][element.find('^') + 1])
    return max_coefficient

def GetArray(max_coefficient, array, from_array):
    if from_array[len(from_array) - 2].isdigit():
        array.append(from_array[len(from_array) - 2])
    else:
        array.append(0)

    for element in from_array:
        if element.find('x') > 0:
            array.append(element.replace('x', ''))
    if len(array) < 2:
        array.append(0)

    coefficient = 2

    while coefficient <= max_coefficient:
        for element in from_array:
            if element.find('y^' + str(coefficient)) > 0:
                array.append(element.replace('y^' + str(coefficient), ''))
        if len(array) < coefficient:
            array.append(0)
        coefficient += 1

def main():
    first_file = open('file_01.txt', 'w')
    first_file.write('29x^5 + 45x^4 + 88x^3 + 77x^2 + 55x + 42 = 0')
    first_file.close

    second_file = open('file_02.txt', 'w')
    second_file.write('63x^5 + 24x^4 + 9x^3 + 70x^2 + 52x + 14 = 0')
    second_file.close

    first_file = open('file_01.txt', 'r')
    first_equation = first_file.readline().replace(' = ', ' + ').replace('x^', 'y^').split(' + ')
    first_file.close

    second_file = open('file_02.txt', 'r')
    second_equation = second_file.readline().replace(' = ', ' + ').replace('x^', 'y^').split(' + ')
    second_file.close

    max_coefficient = 0

    max_coefficient = GetMaxCoefficient(max_coefficient, first_equation)
    max_coefficient = GetMaxCoefficient(max_coefficient, second_equation)

    result = []
    first_array = []
    second_array = []

    GetArray(max_coefficient, first_array, first_equation)
    GetArray(max_coefficient, second_array, second_equation)

    first_array = list(map(int, first_array))
    second_array = list(map(int, second_array))

    for i in range(len(first_array)):
        result.append(first_array[i] + second_array[i])

    result.reverse()
    result = list(map(str, result))


    for i, element in enumerate(result):
        if element != '0':
            result[i] = (element + 'x^' + str(max_coefficient - i)).replace('x^1', 'x').replace('x^0', '')


    result = ' + '.join(result) + ' = ' + str(int(first_equation[len(first_equation) - 1]) + int(second_equation[len(second_equation) - 1]))

    result_file = open('file_03.txt', 'w')
    result_file.write(result)
    result_file.close


if __name__ == "__main__":
    main()

