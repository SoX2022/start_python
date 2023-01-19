# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    
#     *Пример:*
    
#     - 6782 -> 23
#     - 0,56 -> 11


def GetFloatValue(message):
    value = input(message)
    print(value[0] == '-')
    if value[0] == '-':
        temp = value.replace('-','', 1)
    else:
        temp = value
    while not temp.replace('.','', 1).isdigit():
        value = input('Value must be a number. Try again: ')
    return float(value)


def HM6():
    user_number = GetFloatValue('Enter your number: ')
    print(f'{user_number}', end=' -> ')

    sum = 0
    user_number = str(user_number).replace('.', '').replace('-', '')
    for i in range (len(user_number)):
        sum += int(user_number[i])
    print(sum)



def HM25():
    q = list(map(int,filter(lambda x: x not in ('-', '.', ','), input('Enter your number: '))))
    print(f'Sum = {sum(q)}')


def main():
    HM25()



if __name__ == "__main__":
    main()

