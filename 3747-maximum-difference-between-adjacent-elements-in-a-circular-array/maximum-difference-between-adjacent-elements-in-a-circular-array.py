class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            diff=nums[i-1]-nums[i]
            res=max(res,abs(diff))
        return res