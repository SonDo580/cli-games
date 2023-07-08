import random
import string

from constants import HANGMAN_PICS, WORDS

all_letters = string.ascii_lowercase


def get_random_word(words):
    index = random.randint(0, len(words) - 1)
    return words[index]


def take_guess(already_guessed):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print('Please enter a single letter!')
        elif guess not in all_letters:
            print('Please enter a letter!')
        elif guess in already_guessed:
            print('You already guessed that letter!')
        else:
            return guess


def get_feedback(secret_word, current, missed_letters, guess):
    missed = False
    if guess not in secret_word:
        missed_letters += guess
        missed = True
    else:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                current[i] = guess
    return (missed, missed_letters, current)


def display_feedback(missed_letters, current):
    print(f'Missed letters: {missed_letters}')
    print(f'Current: {"".join(current)}')


def draw_hangman(pic_index):
    print(HANGMAN_PICS[pic_index])


def round():
    secret_word = get_random_word(WORDS)
    blanks = ['_'] * len(secret_word)
    missed_letters = ''
    current = blanks
    already_guessed = []
    pic_index = 0

    while True:
        draw_hangman(pic_index)
        display_feedback(missed_letters, current)
        print('-' * 20)

        if pic_index == len(HANGMAN_PICS) - 1:
            return (False, secret_word)

        guess = take_guess(already_guessed)
        already_guessed.append(guess)
        missed, missed_letters, current = get_feedback(
            secret_word, current, missed_letters, guess)

        if secret_word == ''.join(current):
            return (True, secret_word)

        if missed:
            pic_index += 1


def print_result(win, secret_word):
    if win:
        print('You won! Congratulation!')
    else:
        print(f"You lost! The secret word is '{secret_word}'.")


def ask_play_again():
    while True:
        answer = input("Press 'y' to play again, 'n' to cancel: ")
        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            return False


def game():
    while True:
        win, secret_word = round()
        print_result(win, secret_word)
        play_again = ask_play_again()
        if not play_again:
            break


game()
