print("Artemii Kolomiichuk, IPZ_Group_7")

import random

NUMBER = random.randint(1, 100)
guess = -1
guesses = 1
while guess != NUMBER:
    guess = int(input())
    if guess > NUMBER:
        print("Менше")
        guesses += 1
    elif guess < NUMBER:
        print("Більше")
        guesses += 1
    else:
        print(f"Кількість спроб: {guesses}")