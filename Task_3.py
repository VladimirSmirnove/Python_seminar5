# Создайте программу для игры в ""Крестики-нолики"".


path = '/Users/inferno163/Documents/Учеба/ДЗ/2 semestr/Python/Seminar(python)_5.py/3_board_file.txt'
board_file = open(path,'r')
board = board_file.read()

print(board)
board_file.close()

board = list(range(1,10))

def draw_board(board):
   with open('/Users/inferno163/Documents/Учеба/ДЗ/2 semestr/Python/Seminar(python)_5.py/3_redak_board.txt', 'w', encoding='utf8') as file:
      print("-" * 13, file=file)
      for i in range(3):
         print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|", file=file)
         print("-" * 13, file=file)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      with open ('/Users/inferno163/Documents/Учеба/ДЗ/2 semestr/Python/Seminar(python)_5.py/3_redak_board.txt', 'a+', encoding='utf8') as file:
         file.write("Куда поставим " + player_token + '? ')


      try:
         player_answer = int(player_answer)
      except:
         with open ('/Users/inferno163/Documents/Учеба/ДЗ/2 semestr/Python/Seminar(python)_5.py/3_redak_board.txt', 'a+', encoding='utf8') as file:
            print("\nНекорректный ввод. Вы уверены, что ввели число?", file=file)

         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            with open ('/Users/inferno163/Documents/Учеба/ДЗ/2 semestr/Python/Seminar(python)_5.py/3_redak_board.txt', 'a+', encoding='utf8') as file:
               print("\nЭта клетка уже занята!", file=file)
      else:
         with open ('/Users/inferno163/Documents/Учеба/ДЗ/2 semestr/Python/Seminar(python)_5.py/3_redak_board.txt', 'a+', encoding='utf8') as file:
               print("\nНекорректный ввод. Введите число от 1 до 9.", file=file)

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)

main(board)
with open ('/Users/inferno163/Documents/Учеба/ДЗ/2 semestr/Python/Seminar(python)_5.py/3_redak_board.txt', 'a+', encoding='utf8') as file:
   print("\nИгра окончена, нажмите enter", file=file)
input("Нажмите Enter для выхода!")


