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

def longestConsecative_better(nums):
    numsSet = set(nums)
    longest_seq = 0

    for n in nums:
        if (n-1) not in numsSet:
            length = 0
            while(n + length) in numsSet:
                length += 1
            longest_seq = max(longest_seq, length)
        
    return longest_seq
    

#print the longest sequence elements
def longestConsecative_better_print(nums):
    numsSet = set(nums)
    longest_seq = 0
    ans  = []


    for n in nums:
        if (n-1) not in numsSet:
            length = 0
            curr_seq_elements = []  # keeping track of current sequence of consecutives
            while(n + length) in numsSet:
                length += 1
                curr_seq_elements.append(n + length - 1)

            if length > longest_seq:  # if the curr_seq is greater than any before then update the length and ans
                longest_seq = length
                ans = curr_seq_elements
        
    print(ans)
    return longest_seq

nums = [9,1,4,7,3,-1,0,5,8,-1,6]
print(longestConsecutive(nums))
print(longestConsecative_better(nums))
print(longestConsecative_better_print(nums))