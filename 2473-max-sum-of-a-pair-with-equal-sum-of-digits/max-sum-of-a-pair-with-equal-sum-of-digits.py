from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
    
        digit_sum_map = defaultdict(int)
        max_sum = -1
        
        def digit_sum(n):
            return sum(int(d) for d in str(n))
        
        for num in nums:
            d_sum = digit_sum(num)
            if d_sum in digit_sum_map:
                max_sum = max(max_sum, num + digit_sum_map[d_sum])
            digit_sum_map[d_sum] = max(digit_sum_map[d_sum], num)
        
        return max_sum