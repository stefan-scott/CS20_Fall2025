# Number Guessing Warmup
# Mr. Scott
# November 6, 2025

# generates a random number from 1 to 100 and stores it in a variable
# repeats the following until the user guesses the number
# gets the user to guess the number (using the ask block)
# tells the user if the number is too high or too low
# congratulates the user when they guess the correct number with a message such as “Way to go! You guessed the right number in 9 tries!”
import random

secret_number = random.randrange(1,101)
user_guess = -1
while user_guess != secret_number:
    user_guess = int(input("Guess? "))
    if user_guess > secret_number:
        print("too high!")
    elif user_guess < secret_number:
        print("too low")
# any code run after the loop
# imply we've guessed the number
print("Congratulations!")
        
    