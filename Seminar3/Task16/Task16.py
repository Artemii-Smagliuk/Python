# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
    # -> 1
from random import randint
n = int(input("Введите размер массива: "))
list_1 = []
for i in range(n):
    list_1.append(randint(0, 10))
print(list_1)
x = int(input("Введите число, у которого считаем количество: "))
sum = 0
for i in list_1:
    if i == x:
        sum += 1
print('->', sum)