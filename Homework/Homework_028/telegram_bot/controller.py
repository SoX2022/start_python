from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, Bot
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from configparser import ConfigParser
import phonebook
import os
import calc


try:
    conf = ConfigParser()
    conf.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
    TOKEN = conf['TOKENS']['python-telegram-bot']
except IndexError:
    print('Error. Missing ".\config.ini".')


class MyBot:
    def __init__(self):
        self.MATH_OPERATORS = ['+', '-', '*', '/', '%']
        self.NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        self.new_update = tuple()
        self.new_context = tuple()
        self.username = 'User'

        self.bot_option = str()

        # calc
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

        # phonebook
        self.phonebook_path = str()
        self.phone_number = str()
        self.first_name = str()
        self.last_name = str()
        self.ph_keyboard = [
            [
                InlineKeyboardButton('Add new phone', callback_data='add')
            ],
            [
                InlineKeyboardButton('Find phone', callback_data='find')
            ],
            [
                InlineKeyboardButton('Delete phone', callback_data='delete')
            ],
            [
                InlineKeyboardButton('Close', callback_data='close')
            ]
        ]
        self.ph_option = str()
        self.get_input = str()
        self.change_input = str()

        self.server_start()


    async def start_calc(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.new_update = update
        self.new_context = context
        self.username = update.effective_user.first_name
        self.bot_option = 'calc'

        await update.message.reply_text(f'Hello, {self.username}!')
        await self.calc_view()


    async def calc_close(self):
        await self.new_update.message.reply_text(f'{self.username}, I hope my math was accurate.\nIf you need to do math again use /calc.\nUse /help to see more.')


    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'{self.username}, you can use:\n/help to see this message again.\n/calc to start calculator.\n/phonebook to enter your phonebook.')


    async def calc_view(self):
        self.keyboard_update()
        self.reply_markup = InlineKeyboardMarkup(self.calc_keyboard)
        await self.new_update.message.reply_text('Calculator v1.0', reply_markup=self.reply_markup)


    async def calc_view2(self):
        self.keyboard_update()
        self.reply_markup = InlineKeyboardMarkup(self.calc_keyboard)
        await self.query_update.callback_query.message.edit_reply_markup(reply_markup=self.reply_markup)


    async def button(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        query_data = query.data
        self.query_update = update

        if self.bot_option == 'calc':

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
                await self.calc_view2()
            else:
                self.settings_restart()
                self.bot_option = str()

                await self.calc_close()

        elif self.bot_option == 'phonebook':
            self.ph_option = query_data
            if self.ph_option == 'close':
                self.bot_option = str()
                self.get_input = str()
                await self.help(self.new_update, self.new_context)
            else:
                await self.new_update.message.reply_text(f'Enter phone number you want to {self.ph_option}.')


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
        if self.bot_option == 'calc':
            self.user_input = ['']
            self.max_index_input = 0
            self.keyboard_update()
        elif self.bot_option == 'phonebook':
            self.phone_number = str()
            self.first_name = str()
            self.last_name = str()
            self.get_input = 'phone'
            self.ph_option = str()
            self.change_input = str()


    async def phonebook(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.new_update = update
        self.new_context = context
        self.username = update.effective_user.first_name
        self.bot_option = 'phonebook'

        await update.message.reply_text(f'Hello, {self.username}!')
        await self.new_update.message.reply_text('Enter the path to your phonebook.\nIf you don`t have any, enter the path you want to create one.')
        await self.new_update.message.reply_text('Your phonebook must have .csv extension. Example:\n\nPhoneNumber;FirstName;LastName\n{phone};{first name};{last name}')


    async def phonebook_main_view(self):
        self.reply_markup = InlineKeyboardMarkup(self.ph_keyboard)
        await self.new_update.message.reply_text('Phonebook v1.0', reply_markup=self.reply_markup)


    async def phonebook_data(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if self.bot_option == 'phonebook':
            if self.phonebook_path == str():
                self.phonebook_path = update.message.text
                phonebook.get_phonebook_path(self.phonebook_path)
                self.get_input = 'phone'
                await self.phonebook_main_view()
            else:
                if self.get_input == 'phone':
                    self.phone_number = update.message.text
                    self.first_name, self.last_name = phonebook.find_phone(update.message.text)
                    self.get_input = 'first_name'
                match self.ph_option:
                    case 'add':
                        match self.change_input:
                            case '':
                                if self.first_name:
                                    self.change_input = '?'
                                    await update.message.reply_text(f'Number {self.phone_number} is alreade exist.\n Do you want to change data? Y\\N')
                                else:
                                    self.change_input = 'y'
                            case '?':
                                self.change_input = update.message.text.lower()

                                if self.change_input == 'y':
                                    phonebook.delete_phone(self.phone_number)
                                elif self.change_input != 'n':
                                    self.change_input = 'n'

                        match self.change_input:
                            case 'y':
                                match self.get_input:
                                    case 'first_name':
                                        self.get_input = 'last_name'
                                        await update.message.reply_text('Enter first name.')
                                    case 'last_name':
                                        self.first_name = update.message.text
                                        self.get_input = str()
                                        await update.message.reply_text('Enter last name.')
                                    case '':
                                        self.last_name = update.message.text
                                        phonebook.save_new_entry(self.phone_number, self.first_name, self.last_name)
                                        await update.message.reply_text(f'Number {self.phone_number} successfully added.')
                                        self.settings_restart()
                                        await self.phonebook_main_view()
                            case 'n':
                                self.settings_restart()
                                await self.phonebook_main_view()
                    case 'find':
                        if self.first_name:
                            await update.message.reply_text(f'{self.first_name} {self.last_name}')
                        else:
                            await update.message.reply_text('Noone have this phone.')
                        self.settings_restart()
                        await self.phonebook_main_view()
                    case 'delete':
                        if self.first_name:
                            phonebook.delete_phone(self.phone_number)
                            await update.message.reply_text(f'Number {self.phone_number} was deleted.')
                        else:
                            await update.message.reply_text('Noone have this phone.')
                        self.settings_restart()
                        await self.phonebook_main_view()



    def server_start(self):
        print('Server started.')
        self.app = ApplicationBuilder().token(TOKEN).build()

        self.app.add_handler(CommandHandler('help', self.help))
        self.app.add_handler(CommandHandler('calc', self.start_calc))
        self.app.add_handler(CommandHandler('phonebook', self.phonebook))

        self.app.add_handler(CallbackQueryHandler(self.button))
        self.app.add_handler(MessageHandler(filters.TEXT, self.phonebook_data))


        self.app.run_polling()

