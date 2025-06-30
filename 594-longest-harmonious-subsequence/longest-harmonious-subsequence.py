class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        res=0
        i,j=0,1
        n=len(nums)
        for j in range(n):
            while nums[j] - nums[i] > 1:
                i += 1
            if nums[j] - nums[i] == 1:
                res = max(res, j - i + 1)
                
        return res
