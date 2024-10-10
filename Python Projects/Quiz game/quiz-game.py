print("Welcome to my Computer Quiz!")

playing = input("Do you want to play? ")

if(playing.lower() != "yes"):           #we give not equal to cuz if the user gives anything other than yes then we want to quit the program
    quit()

print("Ok. Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if(answer.lower() == "central processing unit"):
    print('Correct answer!')
    score += 1 
else: 
    print("Incorrect answer!")

answer = input("What does GPU stand for? ")
if(answer.lower() == "graphics processing unit"):
    print('Correct answer!')
    score += 1 
else: 
    print("Incorrect answer!")

answer = input("What does RAM stand for? ")
if(answer.lower() == "random access memory"):
    print('Correct answer!')
    score += 1 
else: 
    print("Incorrect answer!")

answer = input("What does ROM stand for? ")
if(answer.lower() == "read only memory"):
    print('Correct answer!')
    score += 1 
else: 
    print("Incorrect answer!")


answer = input("What does PSU stand for? ")
if(answer.lower() == "power supply"):
    print('Correct answer!')
    score += 1 
else: 
    print("Incorrect answer!")



print("You got " + str(score) + " questions right!")        # or you can do -> print("Your quiz score is: ", score)
print("You got " + str((score / 5) * 100) + "%.")           # covert score to percentage and to string -> str((score / 5) * 100)