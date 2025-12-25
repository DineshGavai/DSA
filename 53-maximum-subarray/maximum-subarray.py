class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        temp=0
        for i in nums:
            temp+=i
            if temp > max_sum:
                max_sum=temp
            
            if temp < 0:
                temp=0
        return max_sum