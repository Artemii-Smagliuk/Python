# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

print('Введите число N: ', end='')
n = int(input())
k = 0
while 2**k <= n:
    print(2**k, end=' ')
    k += 1