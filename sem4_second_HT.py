import random
# С re не смог разобраться :( Но я не уверен, что это бы сильно облегчило бы работу
# Ну точнее я не понял как это можно тут эффективно применить не зная скок будет цифр в степени и коефе


def get_koef_list_rnd(length: int) -> list:
    koef_list = []
    rnd_range = (-10, 10)
    for i in range(length):
        koef_list.append(random.randint(rnd_range[0], rnd_range[1]))
    last_item_rnd_value = 0
    while last_item_rnd_value == 0:
        last_item_rnd_value = random.randint(rnd_range[0], rnd_range[1])
    koef_list.append(last_item_rnd_value)
    return koef_list


def construct_polynomial(koef_list: list) -> str:
    highest_degree = len(koef_list) - 1
    final_string = ''
    if koef_list[0] > 0:
        final_string = f' + {koef_list[0]}'
    elif koef_list[0] < 0:
        final_string = f' - {abs(koef_list[0])}'

    for degree in range(1, highest_degree + 1):
        if koef_list[degree] != 0 and degree > 1:
            final_string = f'^{degree}' + final_string
        if koef_list[degree] != 0:
            final_string = 'X' + final_string
        if koef_list[degree] > 1 or koef_list[degree] < 0:
            final_string = f'{abs(koef_list[degree])}*' + final_string
        if degree < highest_degree and koef_list[degree] >= 1:
            final_string = f' + ' + final_string
        elif degree <= highest_degree and koef_list[degree] < 0:
            final_string = f' - ' + final_string

    final_string += ' = 0'

    return final_string


def split_polynomial(polynomial: str) -> list:
    splitted_polynomial_list = []
    polynomial = polynomial.replace(polynomial[polynomial.index('='):], '')
    polynomial = polynomial.replace(' ', '')
    left_index: int = 0
    for right_index in range(1, len(polynomial)):
        if polynomial[right_index] == '+' or polynomial[right_index] == '-':
            splitted_polynomial_list.append(polynomial[left_index:right_index])
            left_index = right_index

        if right_index == len(polynomial) - 1:
            splitted_polynomial_list.append(polynomial[left_index:])

    splitted_polynomial_list = [i.strip('+').upper() for i in splitted_polynomial_list]

    return splitted_polynomial_list


def get_degrees_koefs_dictionary(polynomial: list) -> dict:
    tmp_dict = {}

    for item in polynomial:

        is_positive_number = True
        if item.__contains__('-'):
            is_positive_number = False
            item = item.replace('-', '')

        if item.__contains__('^'):
            tmp_list: list = item.split('^')
            current_index = tmp_list[0]
            current_degree: int = int(tmp_list[1])
            if current_index == 'X':
                tmp_dict[current_degree] = 1
            else:
                current_index = int(current_index.strip('X*x'))
                tmp_dict[current_degree] = current_index

            if not is_positive_number:
                tmp_dict[current_degree] *= -1

        elif item.__contains__('X'):
            x_index = item.index('X')
            if x_index == 0:
                tmp_dict[1] = 1
            else:
                tmp_dict[1] = int(item[:x_index - 1])

            if not is_positive_number:
                tmp_dict[1] *= -1

        else:
            if int(item) != 0:
                tmp_dict[0] = int(item)

            if not is_positive_number:
                tmp_dict[0] *= -1

    tmp_dict['max'] = max(tmp_dict.keys())
    return tmp_dict


def get_sum_koef_list(polynomial1: dict, polynomial2: dict) -> list:
    max_degree = polynomial1['max']
    if max_degree < polynomial2['max']:
        max_degree = polynomial2['max']
    koef_list = []
    for i in range(max_degree + 1):
        if polynomial1.keys().__contains__(i) or polynomial2.keys().__contains__(i):
            if polynomial1.keys().__contains__(i) and polynomial2.keys().__contains__(i):
                koef_list.append(polynomial1[i] + polynomial2[i])
            elif polynomial1.keys().__contains__(i):
                koef_list.append(polynomial1[i])
            else:
                koef_list.append(polynomial2[i])
        else:
            koef_list.append(0)

    return koef_list


pol1 = construct_polynomial(get_koef_list_rnd(5))
print(pol1)
# pol1 = input("Enter first polynomial: ")

print('')

pol2 = construct_polynomial(get_koef_list_rnd(7))
print(pol2)
#pol2 = input("Enter second polynomial: ")

print('')

dict_koefs_pol1 = get_degrees_koefs_dictionary(split_polynomial(pol1))
dict_koefs_pol2 = get_degrees_koefs_dictionary(split_polynomial(pol2))
print(construct_polynomial(get_sum_koef_list(dict_koefs_pol1, dict_koefs_pol2)))
