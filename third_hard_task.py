
def all_divisors(number):
    divisors_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors_list.append(i)
    return divisors_list


num = int(input("Enter your number: "))
print(f'Your divisors: {all_divisors(num)}')
