from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq=Counter(nums)
        res=0
        for i,cnt in freq.items():
            if cnt > len(nums)//2:
                res=i
        return res