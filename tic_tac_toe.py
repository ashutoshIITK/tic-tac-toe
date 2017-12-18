board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#-----------This Displays the board on your screen-----------#


def disp_board(positions):
    print("_{x1}_|_{x2}_|_{x3}_".format(x1=positions[0],x2=positions[1], x3 =positions[2]))
    print("_{x1}_|_{x2}_|_{x3}_".format(x1=positions[3], x2=positions[4], x3=positions[5]))
    print(" {x1} | {x2} | {x3} ".format(x1=positions[6], x2=positions[7], x3=positions[8]))


#-----------Condition if no one wins the game i.e. the board is full-----------#


def board_full():
    O_X_set = {'X','O'}
    set_of_board = set(board)


#-----------Takes care of all cases in which one wins the game-----------#

def win_check():
    if board[0]==board[1]== board[2]=='O' or board[0]==board[1]== board[2]=='X':
        return True
    elif board[3] == board[4] == board[5] == 'O' or board[3] == board[4] == board[5] == 'X':
        return True
    elif board[6] == board[7] == board[8] == 'O' or board[6] == board[7] == board[8] == 'X':
        return True
    elif board[0] == board[3] == board[6] == 'O' or board[0] == board[3] == board[6] == 'X':
        return True
    elif board[1] == board[4] == board[7] == 'O' or board[1] == board[4] == board[7] == 'X':
        return True
    elif board[2] == board[5] == board[8] == 'O' or board[2] == board[5] == board[8] == 'X':
        return True
    elif board[0] == board[4] == board[8] == 'O' or board[0] == board[4] == board[8] == 'X':
        return True
    elif board[2] == board[4] == board[6] == 'O' or board[2] == board[4] == board[6] == 'X':
        return True

#-----------To replace the numbers on the board with X or O-----------#

def position_store(mark, index):
    global board
    board[index-1] = mark

x = 0
disp_board(board)

while not board_full():
    board_position = int(input("Please enter a number for the board position choice: "))
    if x % 2 == 0:
        position_store('O', board_position)
    else:
        position_store('X', board_position)
    disp_board(board)
    if win_check():
        break
    x += 1
