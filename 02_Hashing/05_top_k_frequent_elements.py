def topKFrequent(nums, k):
        ans = []
        max_key = 1
        hash_mp = {}
        for i in nums:
            if i in hash_mp:
                  hash_mp[i] += 1
            else:
                hash_mp[i] = 1
        
        for i in range(0,k):
            max_key = max(hash_mp,key=hash_mp.get)

            ans.append(max_key)
            hash_mp.pop(max_key)    
            max_key = 1
        
        return ans


def topKFrequent_opt(nums,k):
     hash_mp = {}
     freq_arr = [[] for i in range(len(nums)+1)] ## Defining the bucket array
     ans = []
     for i in nums:
          hash_mp[i] = 1 + hash_mp.get(i,0)
    
     for ele,ind in hash_mp.items():  # Initialize the bucket array with the frequencies and elements
          freq_arr[ind].append(ele)

     for ele in reversed(freq_arr):
          for n in ele:
               ans.append(n)
               k -= 1
               if k == 0:
                    return ans 

nums = [1,1,1,2,2,3]
k = 1
print(topKFrequent(nums,k))
print(topKFrequent_opt(nums,k))
        
