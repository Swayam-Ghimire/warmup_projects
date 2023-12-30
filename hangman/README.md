## Hangman Game
*This Python script implements a simple Hangman game where the player tries to
guess a word letter by letter. The player has a limited number of lives, and 
for each incorrect guess, a life is deducted. The objective is to guess the 
word before running out of lives.*
---
### Sample run
````
You have 8 lives left and you have already used  
Your current word: _ _ _ _
Enter any alphabet: q

The letter q is not in the word.
You have 7 lives left and you have already used  q
Your current word: _ _ _ _
Enter any alphabet: a

The letter a is not in the word.
You have 6 lives left and you have already used  a,q
Your current word: _ _ _ _
Enter any alphabet: b

The letter b is not in the word.
You have 5 lives left and you have already used  a,q,b
Your current word: _ _ _ _
Enter any alphabet: c

The letter c is in the word.
You have 5 lives left and you have already used  a,q,c,b
Your current word: _ _ c _
Enter any alphabet: e

The letter e is in the word.
You have 5 lives left and you have already used  e,q,b,a,c
Your current word: _ _ c e
Enter any alphabet: r

The letter r is in the word.
You have 5 lives left and you have already used  e,q,r,b,a,c
Your current word: r _ c e
Enter any alphabet: a
Guessing of same alphabet twice is not allowed.
You have 5 lives left and you have already used  e,q,r,b,a,c
Your current word: r _ c e
Enter any alphabet: i

The letter i is in the word.
Congratulations!!, you guessed the word: rice
````
