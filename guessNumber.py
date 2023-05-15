import random

MAX_NUM_GUESSES = 6
MIN = 1
MAX = 20

name = input("Hello, what's your name? ")

print(f"Well, {name}, I'm thinking of a number between {MIN} and {MAX}")
rand = random.randint(MIN, MAX)

num_guesses = 0

while num_guesses <= MAX_NUM_GUESSES:
    num_guesses += 1
    guess = int(input("Take a guess: "))

    if guess > rand:
        print("Too high")
    elif guess < rand:
        print("Too low")
    else:
        print(f"Good job, {name}. You guessed my number in {num_guesses} guesses")
        