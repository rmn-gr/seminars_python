# задача 1 сложная необязательная Посчитать сумму цифр любого целого или вещественного числа.
# Через строку решать нельзя. Можно юзать decimal

from decimal import Decimal

number = Decimal(input('Enter your number: '))
decimal_part = number - number // 1
number //= 1
digits_sum = 0

while number > 0:
    digits_sum += number % 10
    number //= 10

while decimal_part > 0:
    decimal_part *= 10
    current_digit = decimal_part // 1 % 10
    digits_sum += current_digit
    decimal_part -= current_digit

print(f'Sum of digits: {digits_sum}')
