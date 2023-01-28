import logger
import get_data


def export_students(students):
    file = open('Homework\Homework_027\students.csv', 'w',encoding='utf-8')
    file.write('Id;First Name;Last Name;Birthday\n')
    for key in students:
        file.write(f"{key};{students[key]['First Name']};{students[key]['Last Name']};{students[key]['Birthday']}")
    file.close()
    logger.log('students.csv created.')


def export_classes():
    classes = get_data.get_classes()
    students = dict()
    students = get_data.get_all_students()

    file = open('Homework\Homework_027\classes.csv', 'w',encoding='utf-8')
    file.write('Class;Students\n')

    for key, value in classes.items():
        file.write(f'{key};')
        temp = []
        for id in students:
            if id in value:
                temp.append(students[id]['First Name'] + ' ' + students[id]['Last Name'])
        file.write(f"{', '.join(temp)}\n")

    file.close()
    logger.log('classes.csv created.')