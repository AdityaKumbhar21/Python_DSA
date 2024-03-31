
def fibonacci(num):
    count = 0
    num_1 = 0
    num_2 = 1
    if num == 1:
        print(1)
    else:
        while count <= num:
            print(num_1)
            sum = num_1 + num_2
            num_1 = num_2
            num_2 = sum
            count+=1
        
fibonacci(8)

