# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

print('Введите количество журавликов: ', end = ' ')
s = int(input())
if s % 3 != 0 or s // 3 % 2 !=0:
     print('Неверное S')
else:
    print(f"{s} -> {s//3//2}  {s//3*2}  {s//3//2}")
