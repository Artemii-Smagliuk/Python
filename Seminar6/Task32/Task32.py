# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def diap_check(ls, min, max):
    ls_back = list()
    for i in range(len(ls)):
        if max > ls[i] > min:
            ls_back.append(i)
    return ls_back

print(diap_check([1,3,4,5,8,21,43,1,43,2,54,2], 2,44))