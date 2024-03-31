def prime(num):
    count = 0
    for i in range(1, num+1):
        if num  % i == 0:
            count +=1
    if count == 2:
        print("The number is prime")
    else:
        print("The number is not a prime number")

prime(11)