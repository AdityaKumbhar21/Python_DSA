num = int(input("Enter a number: "))

if num == 0:
    print("0 is neither odd nor even.")
    
elif (num % 2 == 0):
    print("The number is even.")
else:
    print("The number is odd.")