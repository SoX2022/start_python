# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


x = input('Enter X coordinate: ')

while not x.replace('-', '').replace('.','').isdigit():
    print('Value must be a number. Try again')
    x = input('Enter X coordinate: ')

y = input('Enter Y coordinate: ')

while not y.replace('-', '').replace('.','').isdigit():
    print('Value must be a number. Try again')
    y = input('Enter Y coordinate: ')

if x == '0' and y == '0':
    print(f'The point ({x};{y}) is in the center of the coordinate axis')
elif x == '0':
    print(f'The point ({x};{y}) is on the y-axis')
elif y == '0':
    print(f'The point ({x};{y}) is on the x-axis')
else:
    x = float(x)
    y = float(y)
    print(f'x={x}; y={y}', end=' -> ')
    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    else:
        print(4)

