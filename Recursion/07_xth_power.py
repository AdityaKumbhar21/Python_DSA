def myPow(x: float, n: int) -> float:
    
    if n ==1:  #Base
        return x
    if n>0:   # edge case if n is -ve
        return x*myPow(x, n-1)
    else:
        return x*myPow(x, n-1)
    

print(myPow(10,4))