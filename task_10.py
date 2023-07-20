# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите
# минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно перевернуть
import random


def get_min_flips_amount(coins):
    reverse_count_false = 0
    for item in coins:
        if item == False:
            reverse_count_false += 1
    reverse_count_true = len(coins) - reverse_count_false
    if reverse_count_true < reverse_count_false:
        return reverse_count_true
    return reverse_count_false


num_coins = int(input("Enter the number of coins: "))
coins_array = [bool(random.getrandbits(1)) for _ in range(num_coins)]

print(coins_array)
print(f'Minimum number of coin flips is {get_min_flips_amount(coins_array)}')
