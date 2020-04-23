from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
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
        marker = input(
            f'Player 1: Would you like to be X or O? ').upper()
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
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position


def replay():
    player_decision = input('Would you like to play again? Y or N: ').upper()
    if player_decision == 'Y':
        return True
    else:
        return False


def ready_to_play():
    player_decision = input('Are you ready to play? Y or N: ').upper()
    if player_decision == 'Y':
        return True
    else:
        return False
