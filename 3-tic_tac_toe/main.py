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
    print('Welcome to Tic-Tac-Toe')
    user_mark, computer_mark = get_marks()


game()