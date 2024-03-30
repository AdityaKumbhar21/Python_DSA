
# my approach
str = "abcdcba"

count = 0

rev_ind = -1

for c in str:
    if(c == str[rev_ind]):
        count+=1
    rev_ind -=1

if(count == len(str)):
    print("String is palindrome")
else:
    print("String is not a palindrome") 



# Better approach
def palindrome_string(str):
    str = str.lower()
    rev_string = ""
    for c in range(len(str)):
        rev_string += str[len(str) - 1 - c]

    if(rev_string == str):
        print("String is palindrome")
    else:
        print("String is not a palindrome")

word = "madam"
palindrome_string(word)