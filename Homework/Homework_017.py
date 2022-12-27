# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def GetPositiveIntegerValue(message):
    value = input(message)
    while not value.isdigit():
        value = input('Value must be integer. Try again: ')
    return int(value)

def GetFactors (number):
    count = 0
    factor = 2
    all_factors = []
    while factor < number + 1:
        for divider in range(2, number + 1):
            if factor % divider == 0:
                count += 1
        if count == 1:
            all_factors.append(factor)
            count = 0
            factor += 1
        else:
            count = 0
            factor += 1
    return all_factors


def main():
    user_number = GetPositiveIntegerValue('Enter the number: ')
    result = []
    factors = GetFactors(user_number)

    while user_number > 1:
        for factor in factors:
            if user_number % factor == 0:
                result.append(factor)
                user_number /= factor
                break

    print(result)


if __name__ == "__main__":
    main()

