from IPython.display import clear_output


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
    while not (marker == 'X' or marke == 'O'):
        marker = input('Player 1: Would you like to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)
