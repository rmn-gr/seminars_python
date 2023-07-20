import random
import time


def readable_check_statement(predicates):
    left_result = False
    right_result = False
    iterator = 0
    while iterator < len(predicates) - 1:
        left_result = predicates[iterator] and predicates[iterator + 1]
        iterator += 1
    left_result = not left_result

    iterator = 0
    while iterator < len(predicates) - 1:
        right_result = not (predicates[iterator]) or not (predicates[iterator + 1])
        iterator += 1

    return left_result == right_result


start_time = time.time()

final_result_indicate = True
for _ in range(100):
    amount_predicates = random.randint(3, 15)
    current_predicates = [bool(random.getrandbits(1)) for _ in range(amount_predicates)]
    result = readable_check_statement(current_predicates)
    if not result:
        final_result_indicate = False
        print(f"Predicates: {current_predicates}")
        print(f"Result: {result}")

if final_result_indicate:
    print('Theorem is proved')
else:
    print('Theorem isn\'t proved')

end_time = time.time()

print(end_time - start_time)
