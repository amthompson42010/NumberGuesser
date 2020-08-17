import random

print("Alex's Number Guessing Game")

# Get a random number that is the answer for the game
answer = random.randint(1, 100)

# Setting number of times guessed
guesses = 0

print("Guess a number between 1 and 100: ")

# User has 100 chances to guess the correct number
while guesses < 100:

    # initiallizing the guess from the user
    guess = 0

    # get the user's input
    userInput = input()

    # Check to make sure the user's input is a number
    if(int(userInput)):
        guess = int(userInput)
    else:
        print("You have entered an incorrect type. Please enter a number value (i.e. Float, Integer, Double).")
        break

    print("Number of chances left: ", 100 - (guesses + 1))

    # Win condition
    if guess == answer:

        print("You have won!")
        print("You have completed the game in ", guesses, " turns")
        break
    
    # Too high of a guess condition
    elif guess > answer:

        print("You guessed ", guess, "Your guess was too high")

    # Too low of a guess condition
    else:

        print("You guessed ", guess, "Your guess was too low")

    # increase the number of guesses made by 1
    guesses += 1

# Lose condition
if not guesses < 100:

    print("Sorry, you have used all of your guesses. The correct number is: ", answer)
