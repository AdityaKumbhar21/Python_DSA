
def removeDuplicates_brute(nums):
        temp = [nums[0]]
      
        n = len(nums)
        for i in range(1,n):
            if nums[i] != nums[i-1]:  # for checking the first occurence of the element
                temp.append(nums[i])
        
        for i in range(0, len(temp)):
         nums[i] = temp[i]
        
        return len(temp)


def removeDuplicates_opt(nums):
    left = 1
    n = len(nums)
    for right in range(1,n):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1
                print(left)
    return left
        

arr = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates_brute(arr))
print(removeDuplicates_opt(arr))