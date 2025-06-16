class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res=-1
        max_val=nums[-1]
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i] >= max_val:
                max_val=nums[i]
            else:
                res=max(res,max_val-nums[i])
                    
        return res
