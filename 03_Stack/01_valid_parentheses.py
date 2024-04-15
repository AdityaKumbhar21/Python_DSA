def isValid(s):
    stack = []   #Initializing a stack
    hash_mp = {         # initializing a hashmap for keeping track of closing and opening braces
        ")" : "(",
        "}" : "{",
        "]": "["
    }

    for c in s:
        if c in hash_mp:   #If the char of s is a closing brace
            if stack and stack[-1] == hash_mp[c]:   # and if the top element is opening for the corresponding closing brace
                stack.pop()
            else:
                return False
        else:
            stack.append(c)  # add the opening element in the stack
    
    return True if not stack else False


s = "[{()}"
print(isValid(s))