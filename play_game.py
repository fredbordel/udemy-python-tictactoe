from game_logic import (display_board,
                        player_input,
                        place_marker,
                        win_check,
                        choose_first,
                        space_check,
                        full_board_check,
                        player_choice,
                        replay,
                        ready_to_play)

print('Welcome to the amazing game of tic tac toe!')

while True:
    game_board = [' '] * 10
    first_player_marker, second_player_marker = player_input()
    turn = choose_first()
    print(f'{turn} will go first.')

    play_game = input('Are you rrrrready to playyyyy? Y or N: ').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, first_player_marker, position)

            if win_check(game_board, first_player_marker):
                display_board(game_board)
                print("Congrats! You've won!")
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("It's a draw!")
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, second_player_marker, position)

            if win_check(game_board, second_player_marker):
                display_board(game_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("It's a draw!")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
