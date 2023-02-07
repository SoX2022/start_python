from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import model
from random import randint

player = ''
field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
game = {'player': '', 'bot': ''}
keyboard = [
        [
            InlineKeyboardButton(field[0][0], callback_data='1'),
            InlineKeyboardButton(field[0][1], callback_data='2'),
            InlineKeyboardButton(field[0][2], callback_data='3')
        ],
        [
            InlineKeyboardButton(field[1][0], callback_data='4'),
            InlineKeyboardButton(field[1][1], callback_data='5'),
            InlineKeyboardButton(field[1][2], callback_data='6')
        ],
        [
            InlineKeyboardButton(field[2][0], callback_data='7'),
            InlineKeyboardButton(field[2][1], callback_data='8'),
            InlineKeyboardButton(field[2][2], callback_data='9')
        ]
]
legal_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_update = ()
my_context = ()
moves_counter = 0
tic_tac_toe_stop = False


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'Hello {update.effective_user.first_name}!\nUse /help to know more about me.')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(
'''Enter /help to get a list of enable commands,
/play_tic_tac_toe to start a tic-tac-toe game.''')


async def mark_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global my_update
    global my_context

    my_update = update
    my_context = context
    new_game()

    keyboard2 = [
        [
            InlineKeyboardButton('X', callback_data='X'),
            InlineKeyboardButton('O', callback_data='O')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard2)
    await update.message.reply_text('Choose one:', reply_markup=reply_markup)


async def game_field(player = 'player') -> None:
    global my_update

    stop = stop_game_check()

    if player == 'player' or stop != 'continue':
        reply_markup = InlineKeyboardMarkup(keyboard)
        await my_update.message.reply_text('Your turn.', reply_markup=reply_markup)

    if stop != 'continue':
        await game_stop(stop)


async def game_stop(winner = 'draw') -> None:
    global my_update
    global tic_tac_toe_stop
    global player

    tic_tac_toe_stop = True

    if player == 'draw':
        await my_update.message.reply_text(f'It`s a draw!.\nTo start again enter /play_tic_tac_toe.\nUse /help for more options.')
    else:
        if player == winner:
            await my_update.message.reply_text('Congratulations! You win.\nTo start again enter /play_tic_tac_toe.\nUse /help for more options.')
        else:
            await my_update.message.reply_text('I am the master of the game! Ha ha!\nTo try again enter /play_tic_tac_toe.\nUse /help for more options.')


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global legal_moves
    global game
    global moves_counter
    global tic_tac_toe_stop
    global player

    query = update.callback_query
    await query.answer()
    query_data = query.data


    if game['player'] == 'X' or game['player'] == 'O':
        if int(query_data) in legal_moves:
            play_move(int(query_data), game['player'])

            await game_field('bot')

            if not tic_tac_toe_stop:
                temp = randint(0, len(legal_moves) - 1)
                bot_move = legal_moves[temp]
                play_move(int(bot_move), game['bot'])

                await game_field('bot')
                await game_field('player')
        else:
            await game_field('player')
    else:
        game['player'] = query_data
        player = query_data

        if query_data == 'X':
            game['bot'] = 'O'

            await game_field('player')
        else:
            game['bot'] = 'X'
            temp = randint(0, len(legal_moves) - 1)
            bot_move = legal_moves[temp]
            play_move(int(bot_move), game['bot'])

            await game_field('bot')
            await game_field('player')


def play_move(move, player):
    global keyboard
    global legal_moves
    global moves_counter

    if move in (1, 2, 3):
        field[0][move - 1] = player
    elif move in (4, 5, 6):
        field[1][move - 4] = player
    else:
        field[2][move - 7] = player

    legal_moves.remove(move)
    moves_counter += 1

    keyboard = [
        [
            InlineKeyboardButton(field[0][0], callback_data='1'),
            InlineKeyboardButton(field[0][1], callback_data='2'),
            InlineKeyboardButton(field[0][2], callback_data='3')
        ],
        [
            InlineKeyboardButton(field[1][0], callback_data='4'),
            InlineKeyboardButton(field[1][1], callback_data='5'),
            InlineKeyboardButton(field[1][2], callback_data='6')
        ],
        [
            InlineKeyboardButton(field[2][0], callback_data='7'),
            InlineKeyboardButton(field[2][1], callback_data='8'),
            InlineKeyboardButton(field[2][2], callback_data='9')
        ]
    ]


def stop_game_check():
    global moves_counter

    if field[0][0] == field[1][1] == field[2][2] != ' ':
        return field[0][0]

    if field[2][0] == field[1][1] == field[0][2] != ' ':
        return field[2][0]

    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] != ' ':
            return field[i][0]

    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i] != ' ':
            return field[0][i]

    if moves_counter == 9:
        return 'draw'

    return 'continue'


def new_game():
    global legal_moves
    global moves_counter
    global tic_tac_toe_stop
    global game
    global keyboard
    global field
    global player

    player = ''
    legal_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    moves_counter = 0
    tic_tac_toe_stop = False
    field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    game['player'] = ''
    game['bot'] = ''
    keyboard = [
            [
                InlineKeyboardButton(field[0][0], callback_data='1'),
                InlineKeyboardButton(field[0][1], callback_data='2'),
                InlineKeyboardButton(field[0][2], callback_data='3')
            ],
            [
                InlineKeyboardButton(field[1][0], callback_data='4'),
                InlineKeyboardButton(field[1][1], callback_data='5'),
                InlineKeyboardButton(field[1][2], callback_data='6')
            ],
            [
                InlineKeyboardButton(field[2][0], callback_data='7'),
                InlineKeyboardButton(field[2][1], callback_data='8'),
                InlineKeyboardButton(field[2][2], callback_data='9')
            ]
    ]



def start_server():
    print('Server is up')
    token = model.get_token()
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler('hello', hello))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('play_tic_tac_toe', mark_choice))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()
