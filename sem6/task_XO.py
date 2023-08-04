# Задача XO необязательная.
# Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
# Конечно, бот не должен ходить на занятые поля
# Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он ходил как можно ближе к своим занятым клеткам
# После каждого хода на экран должна выводиться текущая обстановка на поле.
# Например,
#
from random import randint


def print_field(field, round):
    print()
    print(f'Round: {round}')
    print('- - - - - - -')
    for i in range(3):
        print(f'| {field[i][0]} | {field[i][1]} | {field[i][2]} |')
        print('- - - - - - -')


def check_winner(field, player):
    winner_status = False
    for i in range(3):
        winner_status = winner_status or (field[i][0] == player and field[i][1] == player and field[i][2] == player)
        winner_status = winner_status or (field[0][i] == player and field[1][i] == player and field[2][i] == player)
    winner_status = winner_status or (field[0][0] == player and field[1][1] == player and field[2][2] == player)
    winner_status = winner_status or (field[0][2] == player and field[1][1] == player and field[2][0] == player)
    return winner_status


def is_there_winner(field):
    return check_winner(current_field, 'X') or check_winner(current_field, 'O')


def is_field_full(field):
    is_full = True
    for i in range(3):
        is_full = is_full and '-' not in field[i]
    return is_full


def bot_move(field):
    is_move_done = False
    while not is_move_done:
        bot_step_row = randint(0, 2)
        bot_step_column = randint(0, 2)
        if field[bot_step_row][bot_step_column] == '-':
            field[bot_step_row][bot_step_column] = 'O'
            is_move_done = True


def skin_bag_move(field):
    is_move_done = False
    while not is_move_done:
        user_step_row = int(input('Enter row your move(1-3): ')) - 1
        user_step_column = int(input('Enter column your move(1-3): ')) - 1
        if field[user_step_row][user_step_column] == '-':
            field[user_step_row][user_step_column] = 'X'
            is_move_done = True
        else:
            print('Wrong move! Try again!')


current_field = []
for i in range(3):
    current_field.append(['-', '-', '-'])


skin_bag_move(current_field)
round = 1
while not is_there_winner(current_field) and not is_field_full(current_field):
    bot_move(current_field)
    print_field(current_field, round)
    round += 1
    skin_bag_move(current_field)

print_field(current_field, round)
if check_winner(current_field, 'X'):
    print("X's win!!!")
elif check_winner(current_field, 'O'):
    print("O's win!!!")
else:
    print('Draw!')