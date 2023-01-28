import datetime

def log(message):
    time = datetime.datetime.now().strftime('%D %H:%M:%S')

    with open('Homework\Homework_027\school\log.txt', 'a') as file:
        file.write(f"{time} - {message}\n")
