import view
import functions


def Start():
    current_phonebook = functions.GetDataFromColumns('Homework\Homework_026\Phonebook\PBData.txt')
    stop = False

    while not stop:
        user_choice = view.GetUserChoice()

        # 1 = Add new phone
        if user_choice == '1':
            new_phone = view.GetNewPhone()
            functions.MatchingNumbers(current_phonebook, new_phone)

            # 2 = Import
        elif user_choice == '2':
            path = view.GetFilePath()
                    # 2 = Rows format
            if int(view.GetDataType('import')) - 1:
                new_phones = functions.GetDataFromRows(path)
            else: # 1 = Column format
                new_phones = functions.GetDataFromColumns(path)
            functions.MatchingNumbers(current_phonebook, new_phones)

            # 3 = Export
        elif user_choice == '3':
            path = view.GetFilePath()

                   # 1 = *.csv   2 = *.txt
            if int(view.GetExportFileType()) - 1:
                if int(view.GetDataType('export')) - 1:
                    functions.ExportContactsInTXTColumns(path, current_phonebook)
                else:
                    functions.ExportContactsInCSV(path, '\contacts.txt', current_phonebook)
                    
            else:
                functions.ExportContactsInCSV(path, '\contacts.csv', current_phonebook)
        else: # 4 = Exit
            stop = True

    functions.SaveData(current_phonebook)