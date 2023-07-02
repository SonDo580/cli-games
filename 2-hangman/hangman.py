import random
from hangman_pics import HANGMAN_PICS
from secret_words import WORDS


def get_random_word(words):
    index = random.randint(0, len(words) - 1)
    return words[index]
