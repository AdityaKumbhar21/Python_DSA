from typing import *
def palindromeHelper(s, e, str) -> bool:
    
    if s>=e:
        return True
    
    if str[s] != str[e]:
        return False
    
    return palindromeHelper(s+1, e-1, str)


def isPalindrome(string: str) -> bool:
    size = len(string)
    return palindromeHelper(0,size-1, string)
    
print(isPalindrome("abcd"))