import view
import model
import get_data
import save_data
import export_data


def start():
    student_id_counter = get_data.get_last_student_id()
    user_choice = view.get_user_choice()

    while user_choice.lower() != 'stop':
                         # 1 - добавить нового ученика
        if user_choice == '1':
            # new_student = dict()
            new_student = model.add_new_student(student_id_counter)
            student_id_counter = new_student['Id']
            save_data.save_student(new_student)

                           # 2 - отчислить (удалить) ученика
        elif user_choice == '2':
            model.delete_student()

                           # 3 - экспорт учеников в students.csv'
        elif user_choice == '3':
            export_data.export_students(get_data.get_all_students())

                           # 4 - экспорт классов в classes.csv'
        elif user_choice == '4':
            export_data.export_classes()
                           # 5 - изменение информации о студенте'
        elif user_choice == '5':
            model.info_change()
                           # 6 - перевод студента в другой класс'
        elif user_choice == '6':
            model.student_transfer()
        else: # ошибочный ввод
            view.error()
        user_choice = view.get_user_choice()

    save_data.save_last_student_id(student_id_counter)