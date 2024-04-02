# Recusrion is function that calss itself to perform a specific task

def fn(n):
    if n == 1:
        # This is the base case where we do not call the function 
        return 1
    else:
        # This is a reursive case where the function is called to give sum of n natural numbers
        s = n + fn(n-1)
        return s


print(fn(3))