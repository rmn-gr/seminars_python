# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он
# задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# x*y = c => x*(b-x) = c => -x*x + b*x -c = 0

import math


def get_discriminant(a, b, c):
    return b * b - 4 * a * c


def get_numbers(add_sum, discr):
    return (-add_sum + math.sqrt(discr)) / -2, (-add_sum - math.sqrt(discr)) / -2


addition_sum = int(input("Enter addition sum: "))
multiply_sum = int(input("Enter sum of multiplying: "))

discriminant = get_discriminant(-1, addition_sum, -multiply_sum)

if discriminant >= 0:
    print(f'Your numbers: {get_numbers(addition_sum, discriminant)}')
else:
    print("There are no solutions")
