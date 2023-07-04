import random

SIZE = 3


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


def get_random_int(min, max):
    return random.randint(min, max)


def computer_move(board, computer_mark):
    while True:
        row = get_random_int(0, SIZE - 1)
        col = get_random_int(0, SIZE - 1)

        if board[row][col] == ' ':
            board[row][col] = computer_mark
            return


def game():
    print('Welcome to Tic-Tac-Toe!')
    board = create_board()
    user_mark, computer_mark = get_marks()

    print('The computer will go first.')
    computer_move(board, computer_mark)
    draw_board(board)


game()
