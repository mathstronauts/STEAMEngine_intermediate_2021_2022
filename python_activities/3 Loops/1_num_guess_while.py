"""
 * Copyright (C) Mathstronauts. All rights reserved.
 * This information is confidential and proprietary to Mathstronauts and may not be used, modified, copied or distributed.
"""

# While loop random number guessing game

import random

random_num = random.randint(1, 10)

print("Your job is to guess the secret number.")
print("Enter '0' to quit the game.")
guess = input("Enter guess: ")  # first intialize the cv

while int(guess) != random_num:
    # print("You guessed wrong")  # statement to user

    if int(guess) == 0: # statement to user
        break
    elif int(guess) > random_num:
        print("You guessed too high")  # statement to user
    elif int(guess) < random_num:
        print("You guessed too low")  # statement to user

    guess = input("Enter guess: ")  # update cv


# once the loop ends
print("The secret number was", str(random_num))
