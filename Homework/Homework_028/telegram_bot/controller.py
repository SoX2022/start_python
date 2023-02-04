from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, Bot
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
from configparser import ConfigParser
import os
import calc


try:
    conf = ConfigParser()
    conf.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
    TOKEN = conf['TOKENS']['python-telegram-bot']

except IndexError:
    print('Error. Missing ".\config.ini".')


class BotCalc:
    def __init__(self):
        self.MATH_OPERATORS = ['+', '-', '*', '/', '%']
        self.NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        self.new_update = tuple()
        self.new_context = tuple()
        self.username = 'User'

        self.message_id = int()
        self.chat_id = int()


        self.user_input = ['']
        self.max_index_input = 0
        self.calc_keyboard = [
            [
                InlineKeyboardButton(' ' + ''.join(self.user_input), callback_data='user_input')
            ],
            [
                InlineKeyboardButton('CE', callback_data='CE'),
                InlineKeyboardButton('C', callback_data='C'),
                InlineKeyboardButton('%', callback_data='%'),
                InlineKeyboardButton('←', callback_data='backspace')
            ],
            [
                InlineKeyboardButton('7', callback_data='7'),
                InlineKeyboardButton('8', callback_data='8'),
                InlineKeyboardButton('9', callback_data='9'),
                InlineKeyboardButton('÷', callback_data='/')
            ],
            [
                InlineKeyboardButton('4', callback_data='4'),
                InlineKeyboardButton('5', callback_data='5'),
                InlineKeyboardButton('6', callback_data='6'),
                InlineKeyboardButton('×', callback_data='*')
            ],
            [
                InlineKeyboardButton('1', callback_data='1'),
                InlineKeyboardButton('2', callback_data='2'),
                InlineKeyboardButton('3', callback_data='3'),
                InlineKeyboardButton('-', callback_data='-')
            ],
            [
                InlineKeyboardButton(',', callback_data='.'),
                InlineKeyboardButton('0', callback_data='0'),
                InlineKeyboardButton('=', callback_data='='),
                InlineKeyboardButton('+', callback_data='+')
            ],
            [
                InlineKeyboardButton('Close', callback_data='close')
            ]
        ]

        self.server_start()

    async def start_calc(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.new_update = update
        self.new_context = context
        self.username = update.effective_user.first_name
        await update.message.reply_text(f'Hello, {self.username}!')
        await self.calc_view()

    async def help(self):
        await self.new_update.message.reply_text(f'{self.username}, I hope my math was accurate.\nIf you need to do math again press /start.')


    async def calc_view(self):
        self.keyboard_update()
        self.reply_markup = InlineKeyboardMarkup(self.calc_keyboard)
        await self.new_update.message.reply_text('Calculator v1.0', reply_markup=self.reply_markup)





    # async def calc_view2(self):
    #     self.keyboard_update()
    #     self.reply_markup = InlineKeyboardMarkup(self.calc_keyboard)
    #     await Bot.edit_message_reply_markup(inline_message_id='Calculator v1.0', reply_markup=self.reply_markup)

    # async def calc_view2(self):
    #     self.keyboard_update()
    #     self.reply_markup = InlineKeyboardMarkup(self.calc_keyboard)
    #     await Bot.edit_message_reply_markup(self=Bot, chat_id=self.chat_id, message_id=self.message_id, reply_markup=self.reply_markup)



    async def button(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        query_data = query.data
        self.query_update = update

        self.chat_id = query.message.chat_id
        self.message_id = query.message.message_id

        if query_data == 'backspace':
            if self.user_input != ['']:
                if self.user_input[self.max_index_input] == '':
                    self.user_input.pop(self.max_index_input)
                    self.max_index_input -= 1

                if self.user_input[self.max_index_input] in self.MATH_OPERATORS:
                    self.user_input.pop(self.max_index_input)
                    self.max_index_input -= 1
                else:
                    self.user_input[self.max_index_input] = self.user_input[self.max_index_input][:-1]
        elif query_data in self.NUMBERS:
            self.user_input[self.max_index_input] += query_data
        elif query_data in self.MATH_OPERATORS:
            self.user_input.append(query_data)
            self.user_input.append('')
            self.max_index_input += 2
        else:
            match query_data:
                case '=':
                    calc.Calc(self.user_input)
                    self.user_input = list(map(str, self.user_input))
                    self.max_index_input = 0
                case '.':
                    if self.user_input[self.max_index_input] == '':
                        self.user_input[self.max_index_input] += '0' + query_data
                    else:
                        self.user_input[self.max_index_input] += query_data
                case 'C':
                    self.settings_restart()
                case 'CE':
                    self.user_input.pop(self.max_index_input)
                    self.user_input.append('')

        if query_data != 'close':
            await self.calc_view()
        else:
            self.settings_restart()
            await self.help()


    def keyboard_update(self):
        self.calc_keyboard = [
            [
                InlineKeyboardButton(' ' + ''.join(self.user_input), callback_data='user_input')
            ],
            [
                InlineKeyboardButton('CE', callback_data='CE'),
                InlineKeyboardButton('C', callback_data='C'),
                InlineKeyboardButton('%', callback_data='%'),
                InlineKeyboardButton('←', callback_data='backspace')
            ],
            [
                InlineKeyboardButton('7', callback_data='7'),
                InlineKeyboardButton('8', callback_data='8'),
                InlineKeyboardButton('9', callback_data='9'),
                InlineKeyboardButton('÷', callback_data='/')
            ],
            [
                InlineKeyboardButton('4', callback_data='4'),
                InlineKeyboardButton('5', callback_data='5'),
                InlineKeyboardButton('6', callback_data='6'),
                InlineKeyboardButton('×', callback_data='*')
            ],
            [
                InlineKeyboardButton('1', callback_data='1'),
                InlineKeyboardButton('2', callback_data='2'),
                InlineKeyboardButton('3', callback_data='3'),
                InlineKeyboardButton('-', callback_data='-')
            ],
            [
                InlineKeyboardButton(',', callback_data='.'),
                InlineKeyboardButton('0', callback_data='0'),
                InlineKeyboardButton('=', callback_data='='),
                InlineKeyboardButton('+', callback_data='+')
            ],
            [
                InlineKeyboardButton('Close', callback_data='close')
            ]
        ]


    def settings_restart(self):
        self.user_input = ['']
        self.max_index_input = 0
        self.keyboard_update()


    def server_start(self):
        print('Server started.')
        self.app = ApplicationBuilder().token(TOKEN).build()

        self.app.add_handler(CommandHandler('start', self.start_calc))
        self.app.add_handler(CallbackQueryHandler(self.button))


        self.app.run_polling()

