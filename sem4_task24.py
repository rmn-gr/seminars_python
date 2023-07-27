import random

bushes_number: int = int(input("Enter bushes number: "))
bushes: list = []
for _ in range(bushes_number):
    bushes.append(random.randint(1, 19))

print(bushes)

harvester_position: int = int(input("Enter harvester position: "))

if harvester_position > bushes_number - 1:
    while harvester_position > bushes_number - 1:
        harvester_position -= bushes_number
elif harvester_position < 0:
    while harvester_position < 0:
        harvester_position += bushes_number

if harvester_position == bushes_number - 1:
    print(bushes[harvester_position] + bushes[harvester_position - 1] \
          + bushes[0])
else:
    print(bushes[harvester_position] + bushes[harvester_position - 1] \
          + bushes[harvester_position + 1])
