# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Тот, кто берет последнюю конфету - проиграл.
# игра с другом
 
 
import random
 
game_candy = '2_startgame_candy.txt'
candy_file = open(game_candy,'r')
candy = candy_file.read()
print(candy)
candy_file.close()
 
messages = ['Ваш ход брать конфеты', 'Возьмите конфеты',
            'сколько конфет берем?', 'берите еще', 'Ваш ход']
 
 
def game_friends_vs_friends(total_sweets, max_number_move, players, messages):
    count = 0
    if total_sweets % 10 == 1 and 9 > total_sweets > 10: letter = 'а'
    elif 1 < total_sweets % 10 < 5 and 9 > total_sweets > 10: letter = 'ы'
    else: letter = ''
    first = random.randint(0, 1)
    with open('2_game_candy.txt', 'a+', encoding='utf8') as file:
        print (f'\nПервый ход определён жеребьёвкой, начинает игрок № {first + 1} ', file=file)
 
    while total_sweets > 0:
        move = int(input(f'{players[first % 2]}, {random.choice(messages)}:'))
        with open('2_game_candy.txt', 'a+', encoding='utf8') as file:
            print (f'{players[first % 2]}, {random.choice(messages)}:', file=file)

        if move > total_sweets or move > max_number_move:
            with open('2_game_candy.txt', 'a+', encoding='utf8') as file:
                print(f'Можно взять не более {max_number_move} конфет{letter}, у нас всего {total_sweets} конфет{letter}', file=file)
            chance = 2
            while chance > 0:
                if total_sweets >= move <= max_number_move:
                    break
                with open('2_game_candy.txt', 'a+', encoding='utf8') as file:
                    print(f'Попробуйте ещё раз, у Вас {chance} попытки', file=file)
                move = int(input())
                chance -= 1
                with open('2_game_candy.txt', 'a+', encoding='utf8') as file:
                    print(move, file=file)
            else:
                return print(f'Попыток не осталось. Game over!')
        total_sweets = total_sweets - move
        if total_sweets > 0:
            with open('2_game_candy.txt', 'a+', encoding='utf8') as file:
                print(f'Осталось {total_sweets} конфет{letter}', file=file)
        else:
            with open('2_game_candy.txt', 'a+', encoding='utf8') as file:
                print('Все конфеты разобраны.', file=file)
        first += 1
        count += 1
    return players[first % 2]
 
 
player1 = input('Первый игрок, как к Вам можно обращаться?\n')
with open('2_game_candy.txt', 'w', encoding='utf8') as file:
    print('Первый игрок, как к Вам можно обращаться?', player1, file=file)
player2 = input('Второй игрок, Ваше имя?\n')
with open('2_game_candy.txt', 'a+', encoding='utf8') as file:
    print('Второй игрок, Ваше имя?', player2, file=file)
players = [player1, player2]
 
total_sweets = int(input('Введите cколько всего у нас конфет:\n'))
with open('2_game_candy.txt', 'a+', encoding='utf8') as file:
    print('Введите cколько всего у нас конфет:', total_sweets, file=file)

max_number_move = int(input('Введите количество конфет, которое можно забрать за один ход:\n'))
with open('2_game_candy.txt', 'a+', encoding='utf8') as file:
    print('Введите количество конфет, которое можно забрать за один ход:', max_number_move, file=file)
 
winer = game_friends_vs_friends(total_sweets, max_number_move, players, messages)
if not winer:
    with open('2_game_candy.txt', 'a+', encoding='utf8') as file:
        print('Победителя нет.', file=file)
else:
    with open('2_game_candy.txt', 'a+', encoding='utf8') as file:    
        print(f'Поздравляю! Победил {winer}!', file=file)