# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

def HM1():
    day_number = input('Enter day number: ')

    while not (day_number.isdigit() and int(day_number) > 0 and int(day_number) < 8):
        print('Day number must have integer value in range [1;7]. Try again')
        day_number = input('Enter day number: ')

    print()
    print(f'{day_number} ->', end=' ')
    if day_number in ('6', '7'):
        print('yes')
    else:
        print('no')

def HM25():
    day_number = ''.join(list(filter(lambda x: x in ('6', '7'), input('Enter day number: '))))

    if day_number:
        print('yes')
    else:
        print('no')


def main():
    HM25()


if __name__ == "__main__":
    main()

