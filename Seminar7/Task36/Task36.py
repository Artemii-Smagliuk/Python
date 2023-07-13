# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, 
# как, например, у операции умножения. 

import ast


def print_operation_table(operation, num_rows=6, num_columns=6):
    err = False
    for y in range(1, num_rows + 1):
        for x in range(1, num_columns + 1):
            try:
                print(f'{operation(x, y)} \t', end='')
            except TypeError:
                print('Ошибка данных, введена не функция')
                err = True
                break
        if err:
            break
        print('\n')


flag = True
while flag:
    operation = input("Введите функцию в формате lambda x, y: x * y ")
    try:
        operation = eval(operation)
        flag = False
    except ValueError or SyntaxError or TypeError or NameError:
        print(f'Введён некорректный формат функции, повторите ввод')

print_operation_table(operation)