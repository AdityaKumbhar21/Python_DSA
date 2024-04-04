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
    


# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

def recHelper(start, s):
        if start >= len(s) //2:
            return True
        if(s[start] != s[len(s)-start-1]):
            return False
        return recHelper(start+1, s) 



def isPalindrome(s):
        s = s.lower()
        s = ''.join(e for e in s if e.isalnum())
        if(len(s)<1):
            return True
        
        return recHelper(0, s)


print(isPalindrome("abcd"))