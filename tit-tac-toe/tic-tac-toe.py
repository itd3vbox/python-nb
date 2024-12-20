def board_print(board):
    i = 0
    while i < 3:
        print(board[i])
        i +=1

def board_token_put(board, token):
    i = int(input('Token Row:'))
    j = int(input('Token Col:'))
    if (
        (i < 0 or i > 2)
        or (j < 0 or j > 2)
        or board[i][j] != '-'
    ):
        print('Cannot put token here')
        return False
    else:
        board[i][j] = token
        return True

def board_has_winner(board):
    i = 0
    while i < 3:
        if (
            board[i][0] != '-'
            and board[i][0] == board[i][1] 
            and board[i][1] == board[i][2] 
        ):
            print('Winner Row', i)
            return True
        i += 1
    i = 0
    while i < 3:
        if (
            board[0][i] != '-'
            and board[0][i] == board[1][i] 
            and board[1][i] == board[2][i] 
        ):
            print('Winner Col', i)
            return True
        i += 1

    if (
        board[0][0] != '-'
        and board[0][0] == board[1][1] 
        and board[1][1] == board[2][2] 
    ):
        print('Winner Diagonal 1')
        return True

    if (
        board[0][2] != '-'
        and board[0][2] == board[1][1] 
        and board[1][1] == board[2][0] 
    ):
        print('Winner Diagonal 2')
        return True
    print('No Winner')
    return False

def board_token_get(index):
    if (index + 1) % 2 == 0:
        return '0'
    else:
        return 'X'

def board_reset(board):
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            board[i][j] = '-'
            j += 1
        i += 1

def game_loop(board):
    board_reset(board)
    i = 0
    while (i < 9):
        board_print(board)
        token = board_token_get(i)
        while board_token_put(board, token) == False:
            pass
        if board_has_winner(board):
            return token
        i += 1
    return '-'

def game_print_menu():
    print('Tic Tac Toe!')
    print('[1] - Start a new game')
    print('[2] - Stat')
    print('[3] - Exit')

def game_print_stat(data):
    print('Game stat:')
    print('---X: ', data['player_1_score'])
    print('---0: ', data['player_2_score'])

def game_update_stat(data, token):
    if token == 'X':
        data['player_1_score'] += 1
    elif token == 'O':
        data['player_2_score'] += 1

def game(data):
    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-'],
    ]
    while True:
        game_print_menu()
        selection = int(input('Select number from menu:'))
        if selection == 1:
            token_winner = game_loop(board)
            game_update_stat(data, token_winner)
        if selection == 2:
            game_print_stat(data)
        elif selection == 3:
            return True
        else:
            continue
        
data = {
    "player_1_score": 0,
    "player_2_score": 0
}

game(data)