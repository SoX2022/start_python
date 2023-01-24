import logger
import view


def ExportContactsInCSV(path, file_name, contacts):
    with open(path + file_name, 'w') as file:
        file.write(f'First Name;Last Name;Phone Number;Description\n')
        for i in contacts:
            file.writelines(f"{contacts[i]['First Name']};{contacts[i]['Last Name']};{i};{contacts[i]['Description']}\n")
    logger.Log(f'Export completed. -> {path}{file_name}')


def ExportContactsInTXTColumns(path, contacts):
    with open(path + '\contacts.txt', 'w') as file:
        for i in contacts:
            file.write(f"First Name: {contacts[i]['First Name']}\n")
            file.write(f"Last Name: {contacts[i]['Last Name']}\n")
            file.write(f"Phone Number: {i}\n")
            file.write(f"Description: {contacts[i]['Description']}\n")
            file.write("\n")
    logger.Log(f'Export completed. -> {path}\contacts.txt.')


def SaveData(phonebook):
    with open('Homework\Homework_026\Phonebook\PBData.txt', 'w') as file:
        for key in phonebook:
            file.write(f"{phonebook[key]['First Name']};{phonebook[key]['Last Name']};{key};{phonebook[key]['Description']}\n")
    logger.Log('Data saved.')


def GetDataFromColumns(path):
    with open(path, 'r') as file:
        pb = file.readlines()
    new_pb = {}

    for element in pb:
        temp = element.replace('\n','').split(';')
        new_pb[temp[2]] = {'First Name': temp[0], 'Last Name': temp[1], 'Description': temp[3]}

    logger.Log('Data (columns) copied.')
    return new_pb


def MatchingNumbers(phonebook, new_phones):
    overwrite = ''

    for key in new_phones:
        if key in phonebook:
            if key in phonebook and overwrite != 'y+' and overwrite != 'n+':
                overwrite = view.get_user_changes_option(key, phonebook[key]['First Name'], phonebook[key]['Last Name']).lower()

            if overwrite == 'n' or overwrite == 'n+':
                logger.Log(f'Phone {key} -> change denied.')
            else:
                phonebook[key] = new_phones[key]
                logger.Log(f'Phone {key} -> change completed.')
        else:
            logger.Log(f'Phone {key} -> successfully added.')
    


def GetDataFromRows(path):
    with open(path, 'r') as file:
        temp = file.readlines()
        new_pb = dict()

        for i in range(0, len(temp), 5):
            q = dict()
            q['First Name'] = temp[i].replace('\n', '').replace('First Name: ','')
            q['Last Name'] = temp[i + 1].replace('\n', '').replace('Last Name: ','')
            q['Description'] = temp[i + 3].replace('\n', '').replace('Description: ','')
            new_pb[temp[i + 2].replace('\n', '').replace('Phone Number: ','')] = q

    logger.Log('Data (rows) copied. ')
    return new_pb