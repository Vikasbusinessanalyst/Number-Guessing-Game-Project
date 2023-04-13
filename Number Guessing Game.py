import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the initial number of guesses to 0
num_guesses = 0

# Loop until the player guesses the correct number 
while True:
    # Get the player's guess
    guess = int(input("Guess a number between 1 and 100: "))
    num_guesses += 1
    
    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number in", num_guesses, "guesses.")
        break
    elif guess < secret_number:
        print("Too low! Guess again")
    else:
        print("Too high! Guess again")
