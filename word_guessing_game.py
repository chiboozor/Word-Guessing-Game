# Import the random module
# Get user's name and greet them.
import random

user_name = input("What is your name? ")
print(f"Welcome, and good luck, {user_name.title()}!\n")

# List of words and choosing a random word using random.choice()
words = ['school', 'church', 'mosque', 'train station', 'building', 'louvre', 'eiffel']
word = random.choice(words)

# User is prompted to start guessing the characters of a randomly chosen word
print("Guess the characters of the random word.")


"""
guesses = empty string to hold all the characters guessed by the user.
turns = total number of turns the user has before their luck runs out.
"""
guesses = ""
turns = 12

while turns > 0:
    failed = 0 # number of incorrect character guesses

    """
    the for loop iterates through each character in the word, and prints it if it is in guesses, but prints an underscore if it isn't.
    """
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end=" ")
            failed += 1

    # if user guesses all characters right
    if failed == 0:
        print(f"\nYou win!\nThe word is: {word.title()}.")
        break
        

    """
    1. prompts user for new character.
    2. checks if user wants to quit the current game.
    3. adds characters to the guesses string if user doesn't want to quit.
    """
    guess = input("\nGuess a character (or enter 'quit' to exit): ")
    if guess.lower() == "quit":
        print("Goodbye! Play again sometime.")
        break
    guesses += guess

    # error handling: incorrect guesses.
    if guess not in word:
        turns -= 1
        print(f"\n\tWrong. You have {turns} guesses left.")

    # check if user has lost
    if turns == 0:
        print(f"\nYou lose.\nThe word is {word.title()}.")
