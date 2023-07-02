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
