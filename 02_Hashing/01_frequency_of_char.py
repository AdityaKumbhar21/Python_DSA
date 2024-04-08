#Given an string and find the frequency of char greater than k


def printFreq(string, k):
    hash_char = {}
    chars = []
    for char in string:
        if char in hash_char:
            hash_char[char] += 1
        else:
         hash_char[char] = 1

    for char in hash_char:
        if hash_char[char] >= k:
           chars.append(char)
    return chars


s = "aabscsasa"
k = 2
print(printFreq(s,k))