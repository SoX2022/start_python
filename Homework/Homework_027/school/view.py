def get_new_student_info(message):
    return input(f'Enter {message}: ')


def get_user_choice():
    return input('''1. Add new student.
2. Expel a student.
3. Export students.
4. Export classes.
5. Change student`s info.
6. Transfer student to another class.
Enter "stop" to exit.
''')


def error():
    print('Invalid choise.')
    print()


def print_all_students(students):
    for item in students:
        print(item, end=' - ')
        print(students[item]['First Name'], end=' ')
        print(students[item]['Last Name'])