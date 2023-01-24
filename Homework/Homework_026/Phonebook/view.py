def GetNewPhone():
    first_name = input('First name: ')
    last_name = input('Last name: ')
    phone_number = input('Phone number: ')
    discrioption = input('Description: ')
    new_phone = dict()
    new_phone[phone_number] = {'First Name': first_name, 'Last Name': last_name, 'Description': discrioption}
    return new_phone


def GetUserChoice():
    return input('Choose one:\n1. Add new number\n2. Import file\n3. Export file\n4. Exit\n')


def GetFilePath():
    return input('Enter file path to the file: ')


def GetExportFileType():
    return input('Select file type.\n1. *.csv\n2. *.txt\n')


def GetDataType(message):
    print('1. First_Name_1;Last_Name_1;Phone_1;Descripton_1')
    print('   First_Name_2;Last_Name_2;Phone_2;Descripton_2')
    print()
    print('2. First Name: First_Name_1')
    print('   Last Name:  Last_Name_1')
    print('   Phone Number: Phone_1')
    print('   Description: Descripton_1')
    print()
    print('   First Name: First_Name_2')
    print('   Last Name:  Last_Name_2')
    print('   Phone Number: Phone_2')
    print('   Description: Descripton_2')
    return input(f'Choose the type of data you want to {message}: ')


def get_user_changes_option(phone, first_name, last_name):
    return input(f"{phone} is already exist as {first_name} {last_name}.\nDo you want to overwrite it?\nEnter 'Y+' to accept all.\nEnter 'N+' to denie all.\nY / N / Y+ / N+ : ")