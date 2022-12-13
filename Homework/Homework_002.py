# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


for x in range(2):
    for y in range(2):
        for z in range(2):
            x = bool(x)
            y = bool(y)
            z = bool(z)
            left_expression = not (x or y or z)
            right_expression = not x and not y and not z
            print()
            print(f'X = {x}; Y = {y}; Z = {z}')
            print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z', end=' is ')
            print(left_expression == right_expression)


#   Почему не работает вывод ответа если записать его без дополнительных переменных left & fight expression?
#   print(not (x or y or z) == not x and not y and not z)
#        ^                     ^^^
#   Точнее есть ошибки тут(^)

#   И, если записать так (устранив ошибки), ответ будет некорректный:
#   print(not (x or y or z) == (not x) and not y and not z)
