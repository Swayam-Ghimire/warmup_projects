"""Making the computer guess the number that we thought of..."""
import random


def computer_guess(low, high):
    guess = 0
    hint = ''
    while hint != 'c' and low != high:
        guess = random.randint(low, high)
        hint = input(f'Is {guess} the number you guessed? '
                     f'If Low(l), High(h) and Correct(c):').lower()
        if hint == 'l':
            low = guess + 1
        elif hint == 'h':
            high = guess - 1
    guess = low
    message = f'Computer guessed your number {guess} correctly.'
    print(message)


computer_guess(1, 1000)
