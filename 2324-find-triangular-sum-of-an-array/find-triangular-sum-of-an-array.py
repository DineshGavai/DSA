class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        while len(nums) > 1:
            for j in range(len(nums)-1):
                val=nums[j]+nums[j+1]
                nums[j]=val%10
            nums.pop()
        return nums[0]
        