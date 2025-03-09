import random
import string

from constants import HANGMAN_PICS, WORDS

all_letters: set[str] = set(string.ascii_lowercase)


def get_random_word(words: list[str]) -> str:
    index: int = random.randint(0, len(words) - 1)
    return words[index]


def take_guess(already_guessed: set[str]) -> str:
    while True:
        guess: str = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter!")
        elif guess not in all_letters:
            print("Please enter a letter!")
        elif guess in already_guessed:
            print("You already guessed that letter!")
        else:
            return guess


def get_feedback(
    secret_word: str, current: list[str], missed_letters: str, guess: str
) -> tuple[bool, str, list[str]]:
    missed: bool = False

    if guess not in secret_word:
        missed_letters += guess
        missed = True
    else:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                current[i] = guess

    return (missed, missed_letters, current)


def display_feedback(missed_letters: str, current: list[str]) -> None:
    print(f"Missed letters: {missed_letters}")
    print(f'Current: {"".join(current)}')


def draw_hangman(pic_index: int) -> None:
    print(HANGMAN_PICS[pic_index])


def round() -> tuple[bool, str]:
    secret_word: str = get_random_word(WORDS)
    blanks: list[str] = ["_"] * len(secret_word)
    current: list[str] = blanks

    missed_letters: str = ""
    already_guessed: set[str] = set()
    pic_index: int = 0

    while True:
        draw_hangman(pic_index)
        display_feedback(missed_letters, current)
        print("-" * 20)

        if pic_index == len(HANGMAN_PICS) - 1:
            return (False, secret_word)

        guess: str = take_guess(already_guessed)
        already_guessed.add(guess)
        missed, missed_letters, current = get_feedback(
            secret_word, current, missed_letters, guess
        )

        if secret_word == "".join(current):
            return (True, secret_word)

        if missed:
            pic_index += 1


def print_result(win: bool, secret_word: str):
    if win:
        print("You won! Congratulation!")
    else:
        print(f"You lost! The secret word is '{secret_word}'.")


def ask_play_again() -> bool:
    while True:
        answer = input("Press 'y' to play again, 'n' to cancel: ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False


def game_loop() -> None:
    while True:
        win, secret_word = round()
        print_result(win, secret_word)
        play_again = ask_play_again()
        if not play_again:
            break


if __name__ == "__main__":
    game_loop()
