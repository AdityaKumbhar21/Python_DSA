def containsDuplicate(nums):
        mp = {}
        for i in nums:
           if  i in mp:
               mp[i] += 1
           else:
               mp[i] = 1
      
        for i in mp:
             if mp[i] >= 2:
                  return True
        
        return False


my_arr = [1,2,3,4,1]
print(containsDuplicate(my_arr))