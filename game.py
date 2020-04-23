from IPython.display import clear_output
import random


def display_board(board):

    clear_output()
    # Printing board
    # board = list
    third_row = ""
    second_row = ""
    first_row = ""
    for each in range(1, 4):
        third_row += f'{board[each]}|'
    for each in range(4, 7):
        second_row += f'{board[each]}|'
    for each in range(7, 10):
        first_row += f'{board[each]}|'

    print(f'|{first_row} \n|{second_row} \n|{third_row}')


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Would you like to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
            # full row
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            # full column
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            # full diagonal
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


def choose_first():
    first_player = random.randint(1, 2)
    return(f'Player {first_player}')


def space_check(board, position):
    return board[position] == ""


def full_board_check(board):
    if "" in board:
        print(True)
    else:
        print(False)


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# print(player_input()[0])
# display_board(test_board)
# place_marker(test_board, '$', 1)
# display_board(test_board)
# win_check(test_board, 'X')
# space_check(test_board, 8)
# full_board_check(test_board)
