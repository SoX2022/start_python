# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


def GetPositiveIntegerValue(message):
    value = input(message)
    while not value.isdigit():
        value = input('Value must be integer. Try again: ')
    return int(value)


user_number = GetPositiveIntegerValue('Enter the number of elements: ')

user_list = []
for i in range(-user_number, user_number + 1):
    user_list.append(i)

print(f'Your list is {user_list}')
first_element_possition = GetPositiveIntegerValue('Enter first position for your list: ')
if first_element_possition < 1 or first_element_possition > len(user_list) + 1:
    print('Position if out of the list range. Try again.')
    first_element_possition = GetPositiveIntegerValue('Enter first position for your list: ')

second_element_possition = GetPositiveIntegerValue('Enter first position for your list: ')
if second_element_possition <1 or second_element_possition > len(user_list) + 1:
    print('Position if out of the list range. Try again.')
    second_element_possition = GetPositiveIntegerValue('Enter first position for your list: ')

data = open('Homework_009.txt', 'w')
data.writelines(f'First position = {first_element_possition}\n')
data.writelines(f'Second position = {second_element_possition}\n')
data.close()

print()
product = 1
data = open('Homework_009.txt', 'r')
first_pos = data.readlines(1)
second_pos = data.readlines(1)
data.close()

first_pos = int(first_pos[0].replace('First position = ',''))
second_pos = int(second_pos[0].replace('Second position = ',''))


product = user_list[first_pos - 1] * user_list[second_pos - 1]
print(f'Product of {first_pos} and {second_pos} element of your list is {product}')

