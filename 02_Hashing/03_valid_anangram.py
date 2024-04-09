
def add_hash(s):
    mp = {}
    for i in s:
            if i in mp:
                mp[i] += 1
            else:
              mp[i] = 1
    return mp

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    else:
        mp_s = add_hash(s)
        mp_t = add_hash(t)
        
    
        for char in mp_s:
           if mp_s[char] != mp_t[char]:
               return False
        
        return True


# we are using extra memory for storing hashmap
def isAnagramNo(s,t):
    return sorted(s) == sorted(t)
       
s = 'anagramta'
t = 'nagaramat'

print(isAnagram(s,t))
print(isAnagramNo(s,t))