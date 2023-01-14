# Создайте программу для игры в ""Крестики-нолики"".

def PrintValue(value):
    if value == 'x':
        print("\033[1m\033[31m{}\033[0m".format(value), end='')
    elif value == '○':
        print("\033[1m\033[34m{}\033[0m".format(value), end='')
    else:
        print("\033[2m{}\033[0m".format(value), end='')

def PrintARow(first, second, third):
    print('│  ', end='')
    PrintValue(first)
    print('  │  ', end='')
    PrintValue(second)
    print('  │  ', end='')
    PrintValue(third)
    print('  │')

def PrintGameField(positions):
    print('┌─────┬─────┬─────┐')
    PrintARow(positions[1], positions[2], positions[3])
    print('├─────┼─────┼─────┤')
    PrintARow(positions[4], positions[5], positions[6])
    print('├─────┼─────┼─────┤')
    PrintARow(positions[7], positions[8], positions[9])
    print('└─────┴─────┴─────┘')

def GetUserTurn(mark, positions):
    print(f'Player {mark}`s moove.\nEnter position you want to put {mark}', end=': ')
    position = input()

    while position not in dict.values(positions):
        print(f'Invalid value.\nEnter position you want to put {mark}', end=': ')
        position = input()

    positions[int(position)] = mark

def GameStopCheck(positions):
    for i in 1, 2, 3:
        if positions[i] == positions[i + 3] == positions[i + 6]:
            return positions[i]

    for i in 1, 4, 7:
        if positions[i] == positions[i + 1] == positions[i + 2]:
            return positions[i]

    if positions[1] == positions[2] == positions[9]:
        return positions[1]

    if positions[3] == positions[5] == positions[7]:
        return positions[3]

    return False

def main():
    usermark = 'x'
    positions = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    winner = False

    PrintGameField(positions)
    print('Let the game begins!')

    for turns in range(9):
        GetUserTurn(usermark, positions)
        PrintGameField(positions)
        winner = GameStopCheck(positions)
        if winner:
            break
        elif usermark == 'x':
            usermark = '○'
        else:
            usermark = 'x'

    if winner:
        print(f'The winner is Player {winner}.')
        print('Congratulations!')
    else:
        print('The game was insane!\nIt`s a DRAW!')



if __name__ == "__main__":
    main()

