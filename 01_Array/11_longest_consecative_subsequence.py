def longestConsecutive(nums):
       nums = sorted(nums)
       ans_counter = 1
       longest_seq = ans_counter
       if len(nums) == 0:
        return 0
       for i in range(0,len(nums)-1):
           if nums[i+1] == nums[i] + 1:
                 ans_counter += 1
           else:
             ans_counter = 1
           longest_seq = max(longest_seq, ans_counter)
        
       return longest_seq

def longestConsecative(nums):
    numsSet = set(nums)
    longest_seq = 0

    for n in nums:
        if (n-1) not in numsSet:
            length = 0
            while(n + length) in numsSet:
                length += 1
            longest_seq = max(longest_seq, length)
        
        return longest_seq

nums = [9,1,4,7,3,-1,0,5,8,-1,6]
print(longestConsecutive(nums))