from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for i in strs:
            sorted_string="".join(sorted(i))
            hashmap[sorted_string].append(i)
        return list(hashmap.values())












      