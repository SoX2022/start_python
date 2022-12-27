# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


def GetPositiveIntegerValue(message):
    value = input(message)
    while not value.isdigit():
        value = input('Value must be integer. Try again: ')
    return int(value)


def main():
    import random

    k = GetPositiveIntegerValue('k = ')
    result = 'k = ' + str(k) + ' => '

    random_coefficient = random.randint(0,99)
    if random_coefficient != 0:
        result += str(random_coefficient) + 'x^' + str(k) + ' '

    for polynom in range(k - 1, 1, -1):
        random_coefficient = random.randint(0,99)
        if random_coefficient != 0:
            result += '+ ' + str(random_coefficient) + 'x^' + str(polynom) + ' '
    random_coefficient = random.randint(0,99)
    if random_coefficient != 0:
        result += '+ ' + str(random_coefficient) + 'x '

    random_coefficient = random.randint(0,99)
    if random_coefficient != 0:
        result += '+ ' + str(random_coefficient) + ' = 0'
    else:
        result += ' = 0'
    print(result)


if __name__ == "__main__":
    main()

