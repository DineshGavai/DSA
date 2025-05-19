class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if len(set(nums))==1:
           return "equilateral"
        elif len(set(nums))==2:
            if nums[0]+nums[1] > nums[2] and nums[0]+nums[2] > nums[1] and nums[1]+nums[2] > nums[0]:
                return "isosceles"
            return "none"
        else:
            if nums[0]+nums[1] > nums[2] and nums[0]+nums[2] > nums[1] and nums[1]+nums[2] > nums[0]:
                return "scalene"
            return "none"