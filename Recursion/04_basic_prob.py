def sumN(n):
    if n == 1:
        return 1
    else:
        return n + sumN(n-1)
    
def sumN_odd(n):
    if n == 1:
        return 1
    else:
        return 2*n-1 + sumN_odd(n-1)
    
def sumN_even(n):
    if n == 1:
        return 2
    else:
        return 2*n + sumN_even(n-1)
    
def sumN_square(n):
    if n == 1:
        return 1
    else:
        return n*n + sumN_square(n-1)

print(sumN_square(10))