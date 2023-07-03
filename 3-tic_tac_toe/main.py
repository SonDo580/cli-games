BOARD = [[' '] * 3] * 3


def draw_board(board):
    for i in range(len(board)):
        print('|'.join(board[i]))
        if i < len(board) - 1:
            print('-+-+-')


def get_marks():
    while True:
        user_mark = input('Do you want to be X or O? ').lower()
        if user_mark == 'x':
            computer_mark = 'o'
        elif user_mark == 'o':
            computer_mark = 'x'
        else:
            print('Please enter X or O!')
            continue
        return (user_mark, computer_mark)


def game():
    board = BOARD
    print('Welcome to Tic-Tac-Toe!')
    user_mark, computer_mark = get_marks()
    print('The computer will go first.')
    draw_board(board)


game()
