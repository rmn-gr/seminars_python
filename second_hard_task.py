import random
import time


def check_statement(pred):
    return not any(pred) == all(map(lambda x: not x, pred))


def readable_check_statement(pred):
    left_result = False
    right_result = False
    iterator = 0
    while iterator < len(pred) - 1:
        left_result = pred[iterator] and pred[iterator + 1]
        iterator += 1
    left_result = not left_result

    iterator = 0
    while iterator < len(pred) - 1:
        right_result = not (pred[iterator]) or not (pred[iterator + 1])
        iterator += 1

    return left_result == right_result


start_time = time.time()

final_result = False
for _ in range(1000):
    num_predicates = random.randint(3, 15)
    predicates = [bool(random.getrandbits(1)) for _ in range(num_predicates)]
    result = readable_check_statement(predicates)
    if not result:
        final_result = True
        print(f"Предикаты: {predicates}")
        print(f"Результат: {result}")

if not final_result:
    print('vse zbs')
else:
    print('выше описаны проблемные случаи')

end_time = time.time()

print(end_time - start_time)
