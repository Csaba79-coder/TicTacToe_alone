import sys
import copy


def init_board():
    board = ['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']
    return board


def print_board(board):
    field = []
    for r in board:
        for c in r:
            if c == '.':
                field.append('.')
            elif c == 1:
                field.append('X')
            else:
                field.append('O')
    print('')
    print('     1   2   3')
    print('')
    print('       |   |')
    print(' A   %s | %s | %s' % (field[0], field[1], field[2]))
    print('       |   |')
    print('   ----+---+----')
    print('       |   |')
    print(' B   %s | %s | %s' % (field[3], field[4], field[5]))
    print('       |   |')
    print('   ----+---+----')
    print('       |   |')
    print(' C   %s | %s | %s' % (field[6], field[7], field[8]))
    print('       |   |')
    return


def get_move(board, player):
    if player == 1:
        name = 'X'
    elif player == 2:
        name = 'O'
    try:
        while True:
            turn = input('\nPlease add your (' + name + ') mark to the board, or type quit: ')
            if turn == 'quit':
                sys.exit()
            else:
                turn = list(turn)
                if turn[0] not in 'abcABC' or turn[1] not in '123':
                    print('Please try again... with a valid input for ' + name + ' mark')
                else:
                    row = turn[0]
                    col = int(turn[1])
                    if row in 'aA':
                        row = 0
                        if board[row][col-1] != '.':
                            print('Sorry, that one is already taken! Try again!')
                        else:
                            col = (col-1)
                            return row, col
                    elif row in 'bB':
                        row = 1
                        if board[row][col-1] != '.':
                            print('Sorry, that one is already taken! Try again!')
                        else:
                            col = (col-1)
                            return row, col
                    elif row in 'cC':
                        row = 2
                        if board[row][col-1] != '.':
                            print('Sorry, that one is already taken! Try again!')
                        else:
                            col = (col-1)
                            return row, col
    except KeyboardInterrupt:
        print('Nice one, see you later!')
        sys.exit()


def get_ai_move(board, player):
    pass


def mark(board, player, row, col):
    if (0 <= row) and (row <= 2) and (0 <= col) and (col <= 2):
        if board[row][col] == '.':
            board[row][col] = player
    return board


def has_won(board, player):
    test_board = copy.deepcopy(board)
    wincondition = False
    for i in test_board:
        win_row = 0
        for k in i:
            if k == player:
                win_row += 1
            if win_row == 3:
                wincondition = True
    column_counter = 0
    while column_counter < 3:
        win_column = 0
        for i in test_board:
            if i[column_counter] == player:
                win_column += 1
            if win_column == 3:
                wincondition = True
        column_counter += 1
    if test_board[1][1] == player:
        if (test_board[0][0] == player) and (test_board[2][2] == player):
            wincondition = True
        if (test_board[2][0] == player) and (test_board[0][2] == player):
            wincondition = True
    return wincondition


def is_full(board):
    k = 0
    for i in board:
        k += i.count('.')
    if k == 0:
        return True
    else:
        return False


def print_result(winner, player):
    win_char = 'O'
    if player == 1:
        win_char = 'X'
    if winner == 2:
        if win_char == 'O':
            print('The winner is the one with the (O) mark!')
        else:
            print('The Winner is the one with the (X) mark!')
    elif winner == 1:
        print('\n')
        print('It\'s a tie! Nobody wins!')
    while True:
        retry = input('Would you like to play again? Type in "Y" to continue or "N" to leave the game: ')
        if retry in 'nN':
            exit()
        elif retry in 'yY':
            main_menu()
    return


def player_select(player):
    if player == 1:
        player = 2
    elif player == 2:
        player = 1
    return player


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    winner = 0
    player = 0
    full_board = False
    won = False
    if mode == 'HUMAN-HUMAN':
        player2 = 'human'
        player1 = 'human'
    while True:
        print_board(board)
        player = player_select(player)
        if (player == 2) and (player2 == 'human'):
            row, col = get_move(board, player)
        elif (player == 1) and (player1 == 'human'):
            row, col = get_move(board, player)
        mark(board, player, row, col)
        full_board = is_full(board)
        won = has_won(board, player)
        if won:
            winner = 2
            break
        elif full_board:
            winner = 1
            break
    print_board(board)
    print_result(winner, player)
    sys.exit()


def main_menu():
    print('#########################################################################')
    print('-------------------------------------------------------------------------')
    print('Hello one and all! Ready for some TicTicTac from two Zolis and one Csaba?')
    try:
        while True:
            print('-------------------------------------------------------------------------')
            print('#########################################################################')
            print('1. Player Vs. Player')
            print('====================')
            print('2. Player Vs. Ai')
            print('================')
            print('3. Quit Game')
            print('============')
            start = input('Choose your option: ')
            if start == '1':
                tictactoe_game('HUMAN-HUMAN')
            elif start == '2':
                print('\nNOT PLAYABLE IN THE BETA\n')
            elif start == '3':
                print('\n')
                print('Thanks for playing, see you!')
                print('\n')
                sys.exit()
    except KeyboardInterrupt:
        print(' That\'s one way to close the program...')
        sys.exit()
    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    main_menu()