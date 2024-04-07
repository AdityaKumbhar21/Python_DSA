from typing import *

# ans = []
# def reverseArray(n:int, nums: List[int],ind):
#     if ind < 0:
#         return ans 
#     else:
#        ans.append(nums[ind])    
#        return reverseHelper(n, nums, ind-1)


# Without returning the list

def reverseArray(n:int, nums: List[int],s, e):
    if s>e:
        return 
    else:
       nums[s], nums[e] = nums[e], nums[s]  
       reverseArray(n,nums, s+1, e-1)   
        
my_list = [1,2,3,4]
n = len(my_list)
reverseArray(n, my_list, 0, n-1)
print(my_list)