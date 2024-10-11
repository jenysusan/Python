a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

ch = input("Enter choice: ")

if(ch.lower() == 'add'):
    print("Sum = ", a+b)
elif(ch.lower() == 'sub'):
    print("Difference = ", a+b)
elif(ch.lower() == 'mult'):
    print("Product = ", a+b)
elif(ch.lower() == 'div'):
    print("Quotient = ", a+b)
elif(ch.lower() == 'mod'):
    print("Remainder = ", a%b)
else:
    print("Invalid choice")
