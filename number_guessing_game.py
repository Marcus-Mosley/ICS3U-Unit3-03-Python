#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on September 2020
# This program is a Number Guessing Game with
#   Random Numbers


import random


def main():
    # This function creates a random number and checks if the user's guess
    #   is equal to the generated number

    # Input
    guess = int(input("Enter a number between 0 and 9: "))
    print("")

    # Process & Output
    random_number = random.randint(0, 9)  # A number between 0 and 9
    if guess == random_number:
        print("That is correct, the right number was {0}!" .format(guess))
    else:
        print("That is incorrect, the right number was {0}!"
              .format(random_number))


if __name__ == "__main__":
    main()
