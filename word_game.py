#word game that lets the user guess the word letter by letter(the word is predefined).

import random

def word_game():
    secret_word = "tuple"
    guesses = []
    attempts = 6

    #letter = ["t", "u", "p", "l", "e"]
    print("welcome to the word guessing game")
    while attempts > 0:
    
        print("Attempts left: ", attempts)

        if all(letter in guesses for letter in secret_word):
            print("Congratulations! You got the word.The word is tuple.")
            return # exits the functionnif the guess is correct

        guess = input("Guess a letter(hint: it's a data type typed with parenthesis):").lower()

        if guess in secret_word:
            print("correct guess!")
            
        elif guess in guesses:
            print("You've already guessed the letter")
        
        else:
            print("Incorrect guess, try again")
            attempts -= 1
        guesses.append(guess)
        
    if attempts == 0:
        print("Sorry, you're out of attempts. The word is: ", secret_word)


    
word_game()