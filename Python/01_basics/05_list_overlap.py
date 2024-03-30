list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

ans = []

highest_len = len(list_1)
if(highest_len < len(list_2)):
    highest_len = len(list_2)

for i in range(0,highest_len):
    if(highest_len == len(list_1)):
        if(list_1[i] in list_2):
             ans.append(list_1[i])
    else:
       if(list_2[i] in list_1):
             ans.append(list_2[i]) 

print(ans)