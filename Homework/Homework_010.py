# Реализуйте алгоритм перемешивания списка.


def GetPositiveIntegerValue(message):
    value = input(message)
    while not value.isdigit():
        value = input('Value must be integer. Try again: ')
    return int(value)


def ListShuffle(array):
    import random
    for i in range(len(array)):
        random_index = random.randint(0, len(array) - 1)
        temp = array[i]
        array[i] = array[random_index]
        array[random_index] = temp


user_number = GetPositiveIntegerValue('Enter the number of elements: ')


user_list = [i for i in range(-user_number, user_number + 1)]

# user_list = []
# for i in range(-user_number, user_number + 1):
#     user_list.append(i)

print(user_list)
ListShuffle(user_list)
print(user_list)

