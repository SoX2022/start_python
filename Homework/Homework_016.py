# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}


def GetPositiveIntegerValue(message):
    value = input(message)
    while not value.isdigit() or  not 0 < int(value) < 11:
        value = input('Value must be integer in range [1; 10]. Try again: ')
    return int(value)


def main():
    import decimal

    π = decimal.Decimal('3.1415926535897932384626433832795028')
    user_number = GetPositiveIntegerValue('Enter the precision of the number - 10^{-1} ≤ 10^(-x) ≤10^{-10}. x = ')
    t = '1.'

    for i in range(user_number):
        t += '0'
        
    π = π.quantize(decimal.Decimal(t))
    print(π) 





if __name__ == "__main__":
    main()

