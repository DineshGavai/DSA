class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum=0
        curr_sum=0

        min_sum=float("inf")
        curr_sum2=0
        for i in nums:
            # For maximum
            curr_sum+=i
            max_sum=max(max_sum,curr_sum)
            if curr_sum < 0:
                curr_sum=0

            # for minimum
            curr_sum2+=i
            min_sum=min(min_sum,curr_sum2)
            if curr_sum2 > 0:
                curr_sum2=0
        
        return max(max_sum,abs(min_sum))


