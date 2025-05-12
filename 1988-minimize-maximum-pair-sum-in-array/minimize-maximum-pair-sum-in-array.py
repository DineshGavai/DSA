class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        res=0
        nums.sort()
        n=len(nums)-1

        for i in range(len(nums)):
            res=max(res,nums[i]+nums[n]) 
            n-=1
        return res