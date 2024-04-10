def twoSum(nums, target):
        n = len(nums)
        ans = []
        for i in range(0,n):
                for j in range(i+1,n):
                        if nums[i] + nums[j] == target:
                                ans.append(i)
                                ans.append(j)
        return ans

def twoSum_better(nums, target):
    n = len(nums)
    mp = {}
    for i in range(0,n):
           diff = target - nums[i]
           if diff in mp:
                  return [mp[diff], i]
           mp[nums[i]] = i



my_arr = [3,2,4]
print(twoSum(my_arr,6))
print(twoSum_better(my_arr,6))