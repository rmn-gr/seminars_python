# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# Список можно задавать рандомно
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]
from random import randint


current_list = [randint(-20, 20) for _ in range(10)]
print(current_list)

min_d = int(input('Enter min diapason: '))
max_d = int(input('Enter max diapason: '))

indexes_list = [i for i in range(len(current_list)) if min_d < current_list[i] < max_d]
print(indexes_list)
