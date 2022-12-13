# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


quater = input('Choose a quater: ')

while not (quater.isdigit() and quater in ('1', '2', '3', '4')):
    print('You should enter a positiv integer in range [1;4]. Try again')
    quater = input('Choose a quater: ')

quater = int(quater)
if quater == 1:
    print('Coordinates for the first quater are: X(0;∞] and Y(0;∞]')
elif quater == 2:
    print('Coordinates for the second quater are: X[-∞;0) and Y(0;∞]')
elif quater == 3:
    print('Coordinates for the third quater are: X[-∞;0) and Y[-∞;0)')
else:
    print('Coordinates for the forth quater are: X(0;∞] and Y[-∞;0)')






