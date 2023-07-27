def to_number_system(number: int, number_system: int) -> str:
    result: str = ''
    while number > 0:
        result = str(number % number_system) + result
        number //= number_system
    return result


num = 814
print(to_number_system(num, 2))
print(bin(num))
