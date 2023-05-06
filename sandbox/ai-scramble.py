#!/usr/bin/python3
import random

# Define the word list
word_list = ["apple", "banana", "cherry", "orange", "pear"]

# Define the score and number of incorrect guesses allowed
score = 0
max_guesses = 3

# Define the function to scramble a word
def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return "".join(word)

# Define the game loop
av = len(word_list)
while av > 0:
    # Select a random word from the list
    word = random.choice(word_list)

    # Scramble the word
    scrambled_word = scramble_word(word)

    # Display the scrambled word to the user
    print("Scrambled word:", scrambled_word)

    # Loop to get the user's guess
    for i in range(max_guesses):
        guess = input("Guess the word: ")

        # Check if the guess is correct
        if guess.lower() == word:
            # Increment the score and print a message
            score += 10
            print("Correct! Your score is now", score)
            break
        else:
            # Print a message indicating an incorrect guess
            print("Incorrect guess. Try again.")

    else:
        # If the user has used up all their guesses, print the correct word and deduct points
        score -= 5
        print("Sorry, you're out of guesses. The correct word was", word)
        print("Your score is now", score)

    # Check if the game is over (score is 0 or less)
    if score <= 0:
        print("Game over!")
        break

    av -= 1

print("Congrats! You scored:", score)
