import random

user_wins = 0               # store the user's score
computer_wins = 0           # store the computer's score

options = ['rock', 'paper', 'scissors']         # list of all the game choices

while True:
    user_input = input("Enter rock/paper/scissors or q to quit: ").lower()          # convert input to lower case
    if user_input == 'q':
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)         # assigned values to choices and selected a number from that range

    # FYI we can also use random.choice(options) to get a value from the list

    computer_pick = options[random_number]
    print("Computer picked " + computer_pick + '.')

    if user_input == 'paper' and computer_pick == 'rock':       # only check combinations where user wins
        print("You win!")
        user_wins += 1
    elif user_input == 'rock' and computer_pick == 'scissors':
        print("You win!")
        user_wins += 1
    elif user_input == 'scissors' and computer_pick == 'paper':
        print("You win!")
        user_wins += 1
    else:                                                       # else will be all the combinations where computer wins
        print("Computer wins!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")

