from IPython.display import clear_output

# Printing board
# Board = list


def display_board(board):

    third_row = ""
    second_row = ""
    first_row = ""
    for each in range(1, 4):
        third_row += f'{board[each]}|'
    for each in range(4, 7):
        second_row += f'{board[each]}|'
    for each in range(7, 10):
        first_row += f'{board[each]}|'

    print("-------")
    print(f'|{first_row} \n|{second_row} \n|{third_row}')


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)
