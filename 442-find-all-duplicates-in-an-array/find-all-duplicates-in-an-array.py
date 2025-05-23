class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                res.append(nums[i])
        return res