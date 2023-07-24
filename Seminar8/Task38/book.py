# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

import functions as fs
while True:
    mode = input('\n Комманды телефонной книги:\
                \n 1 - Внести данные\
                \n 2 - Поиск\
                \n 3 - Вывод всего справочника\
                \n 4 - Удалене записи\
                \n 5 - Редактирование записи\
                \n 0 - Выход\
                \n Ввод => ')
    if mode == '0':
        break
    elif mode == '1':
        fs.data_input()
    elif mode == '2':
        fs.data_search(search=input('Введите данные для поиска: '))
    elif mode == '3':
        fs.data_out()
    elif mode == '4':
        fs.data_delete()
    elif mode == '5':
        fs.data_update()
    else:
        print('Неверный ввод. Введите значение из списка')