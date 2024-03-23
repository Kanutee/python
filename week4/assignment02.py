import random

# Secret word
secret_word = "mosiah"

# Initialize variables
correct_guess = False
guess_count = 0
hint = ['_' for _ in range(len(secret_word))]

print("Welcome to the word guessing game!")

# Loop until correct guess
while not correct_guess:
    user_guess = input("What is your guess? ").lower()
    guess_count += 1
    
    # Check if guess has the same length as secret word
    if len(user_guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue
    
    # Check for correct guess
    if user_guess == secret_word:
        print(f"Congratulations! You guessed it!\nIt took you {guess_count} guesses.")
        correct_guess = True
    else:
        print("Your guess was not correct.")
