# Определить индексы элементо в массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума).

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10
res_list = []

for i in range(0, len(list_1)):
    if list_1[i] >= min_number and list_1[i] <= max_number:
        res_list.append(i)
        print(list_1[i])

print(res_list)





