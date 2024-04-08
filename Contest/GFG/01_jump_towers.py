from typing import *

def minJumps(n : int, arr : List[int]) -> int:
        # code here
        mp = {}
        ans = n-1
        for i in range(n-1,-1,-1):
          if arr[i] in mp:
              ans = min(ans, n - (mp[arr[i]] - i))
          else:
              mp[arr[i]] = i
        
        return ans


heights = [1 ,2 ,1 ,3 ,2]
print(minJumps(5,heights))


