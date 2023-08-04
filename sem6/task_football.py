# Задача FOOTBALL необязательная
# Напишите программу, которая принимает на стандартный вход список
# игр футбольных команд с результатом матча и выводит на стандартный
# вывод сводную таблицу результатов всех матчей.
#
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:

# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
# Пример входа:
#
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
#
# Выход будет:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6


def add_game_result(count_table, winner, loser):
    count_table[winner][1] += 1
    count_table[loser][3] += 1
    count_table[winner][4] += 3


def edit_count_table(count_table: dict, game: list):
    left_team = game[0]
    right_team = game[2]
    left_score = int(game[1])
    right_score = int(game[3])
    if left_team not in count_table.keys():
        count_table[left_team] = [0, 0, 0, 0, 0]
    if right_team not in count_table.keys():
        count_table[right_team] = [0, 0, 0, 0, 0]
    count_table[left_team][0] += 1
    count_table[right_team][0] += 1

    if left_score > right_score:
        add_game_result(count_table, left_team, right_team)
    elif right_score > left_score:
        add_game_result(count_table, right_team, left_team)
    else:
        count_table[left_team][2] += 1
        count_table[right_team][2] += 1
        count_table[left_team][4] += 1
        count_table[right_team][4] += 1


count_table = {}

# games_amount = int(input("Enter amount of games: "))
# for _ in range(games_amount):
#     game = input('Enter game result: ').split(';')
#     edit_count_table(count_table, game)
#

games = ["Спартак;9;Зенит;10", "Локомотив;12;Зенит;3", "Спартак;8;Локомотив;15"]
for game in games:
    edit_count_table(count_table, game.split(';'))

for k, v in count_table.items():
    print(f'{k}: {v}')