import view
import logger
import get_data
import save_data


def add_new_student(student_id_counter):
    new_student = dict()
    new_student['Id'] = get_data.get_new_id(student_id_counter)
    new_student['First Name'] = view.get_new_student_info('student`s first name')
    new_student['Last Name'] = view.get_new_student_info('student`s last name')
    new_student['Birthday'] = view.get_new_student_info('student`s birthday')
    logger.log('Student successfully added.')
    add_students_in_classes(new_student['Id'])
    return new_student


def add_students_in_classes(student_id):
    classes = get_data.get_classes()
    student_class = view.get_new_student_info('student`s class')
    if student_class in classes:
        classes[student_class].append(student_id)
        logger.log('New class successfully created.')
    else:
        classes[student_class] = [student_id]
    logger.log('Student successfully added in class.')
    save_data.save_classes(classes)


def delete_student():
    classes = get_data.get_classes()
    student_id = view.get_new_student_info('student`s id you want to expel.\nIf you want to check all students press "look"')
    students = get_data.get_all_students()
    temp = []

    if student_id.lower() == 'look':
        view.print_all_students(students)
        student_id = view.get_new_student_info('student`s id you want to expel: ')

    for cl in classes:
        if student_id in classes[cl]:
            classes[cl].remove(student_id)
            if classes[cl] == []:
                temp.append(cl)
            logger.log('Student remooved from the class.')

    for element in temp:
        classes.pop(element)
        logger.log('Class removed. No students in class.')

    students.pop(student_id, None)
    save_data.save_all_students(students)
    logger.log('Student expeled.')
    save_data.save_classes(classes)


def info_change():
    students = get_data.get_all_students()
    student_id = view.get_new_student_info('student`s id you want to rename.\nIf you want to check all students press "look"')

    if student_id.lower() == 'look':
        view.print_all_students(students)
        student_id = view.get_new_student_info('student`s id you want to rename: ')


    students[student_id]['First Name'] = view.get_new_student_info('student`s first name')
    students[student_id]['Last Name'] = view.get_new_student_info('student`s last name')
    students[student_id]['Birthday'] = view.get_new_student_info('student`s birthday') + '\n'
    logger.log('Student successfully renamed.')
    save_data.save_all_students(students)


def student_transfer():
    classes = get_data.get_classes()
    student_id = view.get_new_student_info('student`s id you want to transfer to another class.\nIf you want to check all students press "look"')
    students = get_data.get_all_students()
    temp = []

    if student_id.lower() == 'look':
        view.print_all_students(students)
        student_id = view.get_new_student_info('student`s id you want to transfer to another class: ')

    for cl in classes:
        if student_id in classes[cl]:
            classes[cl].remove(student_id)
            if classes[cl] == []:
                temp.append(cl)
            logger.log('Student remooved from the class.')

    for element in temp:
        classes.pop(element)
        logger.log('Class removed. No students in class.')

    save_data.save_classes(classes)
    add_students_in_classes(student_id)
    logger.log('Student transfered.')