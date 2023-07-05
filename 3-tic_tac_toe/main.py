import random

SIZE = 3
NUM_WIN = 3


def create_board():
    board = []
    for i in range(SIZE):
        board.append([])
        for j in range(SIZE):
            board[i].append(' ')
    return board


def draw_board(board):
    for i in range(SIZE):
        print('|'.join(board[i]))
        if i < SIZE - 1:
            print('+'.join('-' * SIZE))


def get_marks():
    while True:
        user_mark = input('Do you want to be X or O? ').upper()
        if user_mark == 'X':
            computer_mark = 'O'
        elif user_mark == 'O':
            computer_mark = 'X'
        else:
            print('Please enter X or O!')
            continue
        return (user_mark, computer_mark)


def check_horizontal(board, mark, row, col):
    point = 0
    j = col
    while j > 0:
        j -= 1
        if board[row][j] == mark:
            point += 1

    j = col
    while j < SIZE - 1:
        j += 1
        if board[row][j] == mark:
            point += 1

    return point + 1


def check_vertical(board, mark, row, col):
    point = 0
    i = row
    while i > 0:
        i -= 1
        if board[i][col] == mark:
            point += 1

    i = row
    while i < SIZE - 1:
        i += 1
        if board[i][col] == mark:
            point += 1

    return point + 1


def check_northwest_southeast(board, mark, row, col):
    point = 0
    i = row
    j = col
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        if board[i][j] == mark:
            point += 1

    i = row
    j = col
    while i < SIZE - 1 and j < SIZE - 1:
        i += 1
        j += 1
        if board[i][j] == mark:
            point += 1

    return point + 1


def check_northeast_southwest(board, mark, row, col):
    point = 0
    i = row
    j = col
    while i > 0 and j < SIZE - 1:
        i -= 1
        j += 1
        if board[i][j] == mark:
            point += 1

    i = row
    j = col
    while i < SIZE - 1 and j > 0:
        i += 1
        j -= 1
        if board[i][j] == mark:
            point += 1

    return point + 1


def check_board(board, mark, row, col):
    point1 = check_horizontal(board, mark, row, col)
    point2 = check_vertical(board, mark, row, col)
    point3 = check_northwest_southeast(board, mark, row, col)
    point4 = check_northeast_southwest(board, mark, row, col)
    return point1 >= NUM_WIN or point2 >= NUM_WIN or point3 >= NUM_WIN or point4 >= NUM_WIN


def get_random_int(min, max):
    return random.randint(min, max)


def computer_move(board, computer_mark):
    while True:
        row = get_random_int(0, SIZE - 1)
        col = get_random_int(0, SIZE - 1)
        if board[row][col] == ' ':
            board[row][col] = computer_mark
            return check_board(board, computer_mark, row, col)


def user_move(board, user_mark):
    print('What is your next move?')
    while True:
        try:
            row = int(input("Enter row index: "))
            col = int(input("Enter column index: "))
            if board[row][col] != ' ':
                print('Please choose another cell!')
                continue
            board[row][col] = user_mark
            return check_board(board, user_mark, row, col)
        except ValueError:
            print('Please enter an interger!')


def game():
    print('Welcome to Tic-Tac-Toe!')
    board = create_board()
    user_mark, computer_mark = get_marks()
    print('The computer will go first.')

    computer_move(board, computer_mark)
    draw_board(board)
    user_move(board, user_mark)
    draw_board(board)


game()
