
def missingNumber_brute(nums):
        n = len(nums)
        temp  = []
        for i in range(0,n+1):
            temp.append(i)
        
        for i in range(0,n):
            if nums[i] == temp[nums[i]]:
                 temp[nums[i]] = -1

        for i in temp:
             if i != -1:
                  return i

def missingNumber_opt(nums):
      
       n = len(nums)
       req_sum = (n*(n+1)) // 2
       sum = 0
       for i in nums:
            sum+= i
       
       return req_sum - sum



arr = [1,3,4,5,2,0]
print(missingNumber_brute(arr))
print(missingNumber_opt(arr))