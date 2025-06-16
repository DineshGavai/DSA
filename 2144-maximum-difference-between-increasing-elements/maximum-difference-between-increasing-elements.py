class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        if sorted(nums,reverse=True)==nums:
            return -1
        res=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    res=max(res,nums[j]-nums[i])
                    
        return res
