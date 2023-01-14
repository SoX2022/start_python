# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


def PlayerTurn(max_number, max_per_turn, player):
    print(f'{player}, How many candies do you want to take? ', end='')
    number = int(input())

    while number <=0 or number > max_number or number > max_per_turn:
        print(f'You have to take some up to {min(max_per_turn, max_number)} candies at time.')
        print('How many candies do you want to take? ', end='')
        number = int(input())

    return number

def AITurn(max_number, max_per_turn, game):
    from random import randint

    if game == 1:
        ai_turn = randint(1, min(max_number, max_per_turn))
        print(f'AI-7000 took {ai_turn} candies')
        return ai_turn

    if max_number % (max_per_turn + 1):
        print(f'AI-7000 took {max_number % (max_per_turn + 1)} candies')
        return max_number % (max_per_turn + 1)
    ai_turn = randint(1, min(max_number, max_per_turn))
    print(f'AI-7000 took {ai_turn} candies')
    return ai_turn

def GetPlayerName(message):
    return input(f'{message}, enter your name: ')

def GameStopCheck(number, player):
    if number > 0:
        if player == 1:
            player = 2
        else:
            player = 1
        return False, player
    return True, player

def GameSettings():
    print('Choose game:')
    print('1 for PvP')
    print('2 for PvE')
    game = input()

    while game not in ('1', '2'):
        game = input('Please choose which game do you want to play: 1 or 2?')

    if game == '1':
        return 0

    print('Choose difficulty:')
    print('1 for easy')
    print('2 for hard')
    game = input()

    while game not in ('1', '2'):
        game = input('Please choose difficulty you want to play: 1 or 2?')
    
    return int(game)

def main():
    from random import randint

    stop = False
    active_player = randint(1,2)
    game = GameSettings()

    if not game:
        first_player_name = GetPlayerName('Player 1')
        second_player_name = GetPlayerName('Player 2')
    else:
        first_player_name = GetPlayerName('Player')
        second_player_name = 'AI-7000'

    print('Enter how many candies are on the table?')
    candies = int(input())

    print('Enter how many candies can you take in maximum?')
    candies_per_turn = int(input())
    print()

    while not stop:
        if candies:
            print(f'{candies} candies left.')
            if active_player == 1:
                candies -= PlayerTurn(candies,candies_per_turn, first_player_name)
            else:
                if not game:
                    candies -= PlayerTurn(candies,candies_per_turn, second_player_name)
                else:
                    candies -= AITurn(candies,candies_per_turn, game)

        stop, active_player = GameStopCheck(candies, active_player)
        print()

    if active_player == 1:
        active_player = first_player_name
    else: 
        active_player = second_player_name

    print(f'The winner is {active_player}.')

    if not game or active_player == first_player_name:
        print('Congratulations!')
    else:
        print('Don`t give up! You will win next time!')



if __name__ == "__main__":
    main()

