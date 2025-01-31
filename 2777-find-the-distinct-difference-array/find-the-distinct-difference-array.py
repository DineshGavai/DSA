class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res=[]
        # i=1
        for i in range(1,len(nums)+1):
            res.append(len(set(nums[:i]))-len(set(nums[i:])))
        return res