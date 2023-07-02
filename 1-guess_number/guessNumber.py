import random

MAX_NUM_GUESSES = 6
MIN = 1
MAX = 20


def take_guess():
    while True:
        try:
            guess = int(input("Take a guess: "))
            return guess
        except ValueError:
            print('Please enter an interger!')


name = input("Hello, what's your name? ")

print(f"Well, {name}, I'm thinking of a number between {MIN} and {MAX}")
rand = random.randint(MIN, MAX)

correct = False
for i in range(MAX_NUM_GUESSES):
    guess = take_guess()

    if guess > rand:
        print("Too high!")
    elif guess < rand:
        print("Too low!")
    else:
        print(f"Good job, {name}. You guessed my number in {i + 1} guesses.")
        correct = True
        break

if not correct:
    print(f"You lost! The number I was thinking of was {rand}.")
