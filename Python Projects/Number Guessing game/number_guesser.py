# Program generates a random number based on user's limit and user can guess which is the random number. 
# Each time user gets it wrong, help the user by mentioning if he/she needs to go higher or lower
# At the end the number of guesses it took will be displayed.

import random

top_of_range = input("Enter top limit of range of numbers: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)            # converting limit to integer

    if top_of_range <= 0:                       # if limit is <= 0 then print to enter a number >0
        print("Please enter a number greater than 0 next time.")
        quit()
else:
    print("Please enter a number.")             # in case the entered value is not a number
    quit()

random_number = random.randint(0,top_of_range)      # generating a random integer using randint btw 0 and top_of_range

guesses = 0

while True :
    guesses += 1
    user_guess = input("Make a guess: ")                 # making a guess of the number
    if user_guess.isdigit():
        user_guess = int(user_guess)                     # converting guess to an integer
    else:
        print("Please enter a number next time.")   # in case not a digit then print msg and go to next iteration
        continue

    if user_guess ==  random_number:                # check if guess is the random number. If yes then print and exit out of the program
        print("You got it dude!")
        break
    elif user_guess < random_number:                # if guess is lesser/greater then print msg
        print("The number is greater than your guess so you have to go higher!")
    else:
        print("The number is lesser than your guess so you have to go lower!")

print("You got it in", guesses, "guesses")


