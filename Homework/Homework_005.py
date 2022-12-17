# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


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

def GetDistance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


ax = GetFloatValue('Enter X coordinate for A: ')
ay = GetFloatValue('Enter Y coordinate for A: ')
bx = GetFloatValue('Enter X coordinate for B: ')
by = GetFloatValue('Enter Y coordinate for B: ')


print(f'A({ax},{ay}); B({bx},{by}) -> {GetDistance(ax, ay, bx, by)}')



# x1, y1 = list(map(int, input('input coords(x1 y1) for first point separated by space - ').split()))
# x2, y2 = list(map(int, input('input coords(x2 y2) for first points separated by space - ').split()))

# print(round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 3))










