import random

def guessing_game() -> None:
    target = random.randint(0, 100)
    while True:
        guess = int(input("What is your guess? "))
        if guess > target:
            print(f"Your guess of {guess} is too high!")
        elif guess < target:
            print(f"Your guess of {guess} is too low!")
        else:
            print(f"Right!  The answer is {guess}")
            return
