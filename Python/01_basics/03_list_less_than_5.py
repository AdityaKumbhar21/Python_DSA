my_list = [1,2,44,5,12,2,3]
ans = []

num = int(input("Enter a number: "))

for i in my_list:
    if(i <num):
        ans.append(i)

print(ans)