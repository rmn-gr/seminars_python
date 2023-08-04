# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


a = int(input('Enter first element: '))
d = int(input('Enter difference: '))
amount = int(input('Enter amount of elements: '))

ap_list = [(a + d*i) for i in range(amount)]

print(ap_list)