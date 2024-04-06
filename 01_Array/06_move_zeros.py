def moveZeroes_brute(nums):
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]

def moveZeroes_opt(nums):
    l = 0
    
    for r in range(1, len(nums)):
        if nums[l] != 0:
            l+=1
        if nums[l] == 0 and nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

arr = [0,1,0,3,12]
# moveZeroes_brute(arr)
moveZeroes_opt(arr)
print(arr)
