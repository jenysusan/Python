name = input("Enter your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You enter a castle and saw 2 doors red and white. Which do you go through(red/white)? ").lower()

if answer == 'red':
    answer = input("You met a wicked witch who gives you 2 apples that are Orange and Purple. Which do you choose (orange/purple)? ").lower()
    if answer == 'orange':
        print("The orange apple summons a monster and the monster kills you. You lose.")
    elif answer == 'purple':
        print("The purple apple takes you to Thanos and he snaps you away. You lose.")
    else:
        print("That's not a valid option. You lose.")

elif answer == 'white':
    answer = input("You shrink and get into the Quantum realm and Antman gives you a console of 2 buttons, Blue and Yellow. Which do you choose (blue/yellow)? ").lower()
    if answer == 'blue':
        print("You are transported out of the realm and into a room full of the world's riches and a whole castle to yourself. You WIN!")
    elif answer == 'yellow':
        print("You get transported to a dungeon in the realm and are stuck for life there. You lose.")
    else:
        print("That's not a valid option. You lose.")

else:
    print("That's not a valid option. You lose.")

print("Thanks for trying", name)
