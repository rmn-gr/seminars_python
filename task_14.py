# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Enter your power of two: '))

for i in range(1, n + 1):
    current_power = 1
    for j in range(1, i + 1):
        current_power *= 2
    print(current_power)

