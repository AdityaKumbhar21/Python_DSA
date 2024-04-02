def printN_rev(n):
    if n > 0:
        print(n, end=' ')
        printN_rev(n-1)

# printN_rev(5)



def print_odd(n):
    if n > 0:
        print_odd(n-1)
        print(2*n-1, end = ' ')

print_odd(10)

def print_even(n):
    if n > 0:
        print_even(n-1)
        print(2*n, end= ' ')

print_even(6)