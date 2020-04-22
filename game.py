from IPython.display import clear_output

# Printing board
# Board = list


def display_board(board):
    for each in board:
        print(' | |')
        print(f'| {each} |')
        print(' | |')


test_board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)
