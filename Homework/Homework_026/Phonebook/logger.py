from datetime import datetime


def Log(message):
    time = datetime.now().strftime('%D %H:%M:%S')
    with open('Homework\Homework_026\Phonebook\log.txt', 'a') as file:
        file.write(f'{time} - {message}\n')