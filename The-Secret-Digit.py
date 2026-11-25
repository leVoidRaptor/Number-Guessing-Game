
# Importing Libraries
import random

# Game Introduction
print("Welcome to The Secret Digit!")

# Main Game Loop
while True:

    # Start or Exit
    start = input("Press S to continue or F to exit: ").strip().upper()

    if start == "S":

        # Generating Random Number
        comp_num = random.randint(0, 100)

        # Game Instructions
        print("The computer has selected a random number. You have 3 attempts to guess it!")

        # Initializing Attempt Counter
        attempts = 0
        guesses = 0

        # First, Second and Third Guesses
        while attempts < 3:

            guess_names = ["First", "Second", "Third"]
            guess = input(f"{guess_names[attempts]} guess: ").strip()

            # Input Validation
            try:
                guess = int(guess)

                if guess < 0 or guess > 100:
                    print("Invalid input! Enter a number between 0 and 100")
                    continue

            except ValueError:
                print("Invalid input! Please enter a valid integer")
                continue

            # Counting Attempts
            attempts += 1

            # Checking the Guess
            if comp_num == guess:
                print("Correct! You guessed the number!")
                print(f"Number: {comp_num}\tYour guess: {guess}")
                print("Attempts:", attempts)
                guesses = 1
                break

            elif comp_num > guess:
                print("Your guess is too low! Try again")

            else:
                print("Your guess is too high! Try again")

        # Game Over
        if guesses == 0:
            print("You couldn't guess the number this time!")
            print("Number:", comp_num)
            print("Attempts:", attempts)

        # Play Again
        while True:
            play_again = input("Do you want to play again? (Y/N): ").strip().upper()

            if play_again == "Y":
                break

            elif play_again == "N":
                print("Goodbye!")
                exit()

            else:
                print("Invalid input! Please press Y or N")

    # Exit Game
    elif start == "F":
        print("Goodbye!")
        break

    # Invalid Input Handling
    else:
        print("Invalid input! Please press S to continue or F to exit")