path = str()


def save_new_entry(phone_number, first_name, last_name):
    global path

    with open(path, 'a') as file:
        file.write(f'{phone_number};{first_name};{last_name}\n')


def find_phone(phone_number):
    global path

    with open(path, 'r') as file:
        phones = file.readlines()

    for row in phones:
        row = row.split(';')

        if row[0] == phone_number:
            return row[1], row[2].replace('\n', '')
    return False, False


def delete_phone(phone_number):
    global path

    with open(path, 'r') as file:
        phones = file.readlines()

    for i, row in enumerate(phones):
        row = row.split(';')
        if row[0] == phone_number:
            phones.pop(i)

    with open(path, 'w') as file:
        for row in phones:
            file.write(f'{row}')


def get_phonebook_path(pth='Homework\Homework_028\\telegram_bot\phonebook\phones.csv'):
    global path

    path = pth
