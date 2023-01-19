# 39(2). Создайте программу для игры в ""Крестики-нолики"". Игра 
# реализуется в терминале, игроки ходят поочередно, необходимо 
# вывести карту(как удобнее, можно например в виде списка, 
# внутри которого будут 3 списка по 3 элемента, каждый из которого 
# обозначает соответсвующие клетки от 1 до 9), сделать проверку не 
# занята ли клетка, на которую мы хотим поставить крестик или нолик, и 
# проверку на победу( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)

def draw_board():
    board_size = 3
    for i in range(board_size):
        print(board[i*board_size], board[1 + i*3], board[2 + i*3])

def start_game():
    currentPlay = 'X'
    step = 1
    draw_board()
    while (step < 10) and (checkWin() == False):
        index = input('Ходит текщий игрок ' + currentPlay + '.Введите число:' + ' ')
        if (game_step(int(index), currentPlay)):        
                if(currentPlay == 'X'):
                    currentPlay = 'O'
                else:
                    currentPlay = 'X'
                draw_board()
                step += 1
        else:
            print('Неверный номер! Повторите')
    if (step == 10): print(f'Ничья')
    else: print(f'Выйграл - > {checkWin()}')

def checkWin():
    win = False
    for i in winCombination:
        if(board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]]):
            win = board[i[0]]
    return win

def game_step(index, char):
    if(index > 9 or index < 1 or board[index - 1] in ('X', 'O')):
        return False
    else: 
        board[index - 1] = char
        return True


board = [1,2,3,4,5,6,7,8,9]
winCombination = (
        (0,1,2),
        (3,4,5),
        (6,7,8),

        (0,3,6),
        (1,4,7),
        (2,5,8),

        (0,4,8),
        (2,4,6)
)

print('Добро пожаловать в крестики нолики!')
start_game()