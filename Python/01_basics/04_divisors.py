num = int(input("Enter a number: "))

print("The divisors for number", num , " between 1 to 10 are: ")

for i in range(1,11):
    if(i % num == 0):
        print(i)
