class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res |= num
        return res