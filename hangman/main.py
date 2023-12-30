import random
from json import words
import time


def get_valid_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.lower()


def hangman():
    word = get_valid_word()
    letters = set(word)
    alphabets = 'abcdefghijklmnopqrastuvwxyz'
    guessed_letters = set()
    lives = len(letters) + 4

    while len(letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have already used ", ','.join(guessed_letters))
        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print("Your current word:", ' '.join(word_list))

        guessed_letter = input('Enter any alphabet: ').lower()
        if guessed_letter in set(alphabets) - guessed_letters:
            guessed_letters.add(guessed_letter)
            if guessed_letter in letters:
                time.sleep(1)
                print(f'\nThe letter {guessed_letter} is in the word.')
                letters.remove(guessed_letter)
            else:
                lives = lives - 1
                time.sleep(1)
                print(f'\nThe letter {guessed_letter} is not in the word.')
        elif guessed_letter in guessed_letters:
            print("Guessing of same alphabet twice is not allowed.")
        else:
            print("Invalid input!!")
    if lives == 0:
        print("Sorry !! , you failed to guess the word:", word)
    else:
        print("Congratulations!!, you guessed the word:", word)


hangman()
