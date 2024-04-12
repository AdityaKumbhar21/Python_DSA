
def productExceptSelf(nums):
    zero_count = 0
    ans = []
    prod = 1
    for num in nums:
       if num != 0:
           prod *= num
       else:
           zero_count += 1
    
    if zero_count > 1:   # if there are more than 1 zero then
        return [0] * len(nums)
    

    for num in nums:
        if num != 0:
            if zero_count == 1:
                ans.append(0)
            else:
                ans.append(prod // num)
        else:
            ans.append(prod)  # for adding the total product at the place of zero in the array
    
    return ans


def productExceptSelf_opt(nums):
    ans = [1] * len(nums)
    prefix = 1
    for i in range(0, len(nums)):
        ans[i] = prefix  #calculating the prefix and storing it in array on the way
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums) - 1, -1 , -1):
        ans[i] *= postfix  # calculating prefix *postfix
        postfix *= nums[i]
    
    return ans

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))
print(productExceptSelf_opt(nums))