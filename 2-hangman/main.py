import random
import string

from hangman_pics import HANGMAN_PICS
from secret_words import WORDS

all_letters = string.ascii_lowercase


def get_random_word(words):
    index = random.randint(0, len(words) - 1)
    return words[index]


def take_guess(already_guessed):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess not in all_letters:
            print('Please enter a letter')
        elif guess in already_guessed:
            print('You already guessed that letter')
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


def game():
    secret_word = get_random_word(WORDS)
    blanks = ['_'] * len(secret_word)
    missed_letters = ''
    current = blanks
    already_guessed = []
    pic_index = 0

    while True:
        guess = take_guess(already_guessed)
        already_guessed.append(guess)
        missed, missed_letters, current = get_feedback(
            secret_word, current, missed_letters, guess)

        if missed:
            pic_index += 1
        if pic_index == len(HANGMAN_PICS) - 1:
            break

        draw_hangman(pic_index)
        display_feedback(missed_letters, current)

    print('Game over')


game()
