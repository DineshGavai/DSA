class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elem_sum=sum(nums)
        digit_sum=0
        for i in nums:
            while i > 0:
                digit_sum+=i%10
                i//=10
        return abs(elem_sum-digit_sum)