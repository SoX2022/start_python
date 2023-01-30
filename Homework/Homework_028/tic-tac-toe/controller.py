from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import model
from random import randint


player = ' '
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
enable_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]




async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'Hello {update.effective_user.first_name}!\nUse /help to know more about me.')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(
'''Enter /help to get a list of enable commands,
/play to start a tic-tac-toe game.''')


async def mark_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard2 = [
        [
            InlineKeyboardButton('X', callback_data='X'),
            InlineKeyboardButton('O', callback_data='O')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard2)
    await update.message.reply_text('Choose one:', reply_markup=reply_markup)



async def game_field(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Your turn.', reply_markup=reply_markup)


# bot: Bot, 
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    query = update.callback_query.data
    # await query.answer()
    # await query.edit_message_text(text=f'Selected option: {query.data}')
    if game['player'] != '':
        play_move(int(query), game['player'])
        temp = randint(0, len(enable_moves) - 1)
        bot_move = enable_moves.pop(temp)
        play_move(int(bot_move), game['bot'])
    else:
        game['player'] = query
        if query == 'X':
            game['bot'] = 'O'
        else:
            game['bot'] = 'X'

# тут нужно вызвать функцию game_field, которая выведет игровое поле в телеграмме и будет ожидать выбор пользователя

    # reply_markup = InlineKeyboardMarkup(keyboard)
    # await Bot.send_message(update.message.chat_id, 'Your turn.', reply_markup=reply_markup)

    # await update.message.reply_text('Your turn.', reply_markup=reply_markup)


def play_move(move, player):
    if move in (1, 2, 3):
        field[0][move - 1] = player
    elif move in (4, 5, 6):
        field[0][move - 4] = player
    else:
        field[0][move - 7] = player







def start_server():
    print('Server is up')
    token = model.get_token()
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler('hello', hello))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('play', mark_choice))
    app.add_handler(CallbackQueryHandler(button))


    app.add_handler(CommandHandler('a', game_field))



    app.run_polling()



