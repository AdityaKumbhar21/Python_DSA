import collections


def groupAnagrams(strs):
    ans_mp = {}
    for s in strs:
      sorted_str = ''.join(sorted(s))
      if sorted_str in ans_mp:
         ans_mp[sorted_str].append(s)
      else:
         ans_mp[sorted_str] = [s]

    return list(ans_mp.values())

def groupAnagrams_better(strs):
   ans_mp = collections.defaultdict(list)

   for s in strs:
      count = [0] *26  #Initialize an array of size 26 to keep up with frequency of elements
      for c in s:
         count[ord(c) - ord("a")] += 1 # adding frequency with each character of string s
      ans_mp[tuple(count)].append(s)

   return list(ans_mp.values())
    



strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))
print(groupAnagrams_better(strs))