from collections import Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for i in strs:
            sorted_string="".join(sorted(i))
            if sorted_string in hashmap:
                hashmap[sorted_string].append(i)
            else:
                hashmap[sorted_string]=[i]
                
        res=[]
        for i in hashmap.values():
            res.append(i)
        return res