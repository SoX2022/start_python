def get_token():
    with open('F:\GB\.token\\telegram_bot.txt', 'r') as file:
        return file.readline()
