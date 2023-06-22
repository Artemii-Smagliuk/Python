# Задача 2: Найдите сумму цифр трехзначного числа. 

print('Введите трехзначное число: ', end = ' ')
num = input()
sum = int(num[0]) + int(num[1]) + int(num[2])
print(f"{num} -> {sum} ({num[0]} + {num[1]} + {num[2]})")