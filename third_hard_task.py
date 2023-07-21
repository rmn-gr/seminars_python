# Нашел вот такое решение в интернетах, сам бы вряд ли додумался до такого
# Насколько вообще имеет смысл подтягивать математику для понимания подобных вещей?
# Или умения пользоваться интернетом будет достаточно? :D
def all_divisors(number):
    divisors_list = []
    for i in range(1, int(number ** 0.5) + 1):
        if i*i == number:
            divisors_list.append(i)
        elif number % i == 0:
            divisors_list.append(i)
            divisors_list.append(number // i)
    return divisors_list


num = int(input("Enter your number: "))
divisors = all_divisors(num)
divisors.sort()
print(f'Your divisors: {divisors}')
