from typing import *

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

# You are given an integer ’n’.
# Your task is to return a sorted array (in increasing order) containing all the factorial numbers which are less than or equal to ‘n’.
    
def factorial_numbers(n) -> List[int]:
    num = 1
    fact = 1
    ans = []
    while fact<=n:
        ans.append(fact)
        num+=1
        fact *= num
    return ans

    


print(factorial(6))