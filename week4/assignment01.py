import random

# Define the secret word
secret_word = "mosiah"

# Initialize variables
correct_guess = False
guess_count = 0

print("Welcome to the Word Guessing Game!")

# Game loop
while not correct_guess:
    user_guess = input("Enter your guess: ").lower()
    guess_count += 1

    # Check if the guess is correct
    if user_guess == secret_word:
        print(f"Congratulations! You've guessed the word '{secret_word}'!")
        print(f"It took you {guess_count} guesses.")
        correct_guess = True
    else:
        print("Sorry, that's not correct. Please try again.")

print("Thanks for playing!")
