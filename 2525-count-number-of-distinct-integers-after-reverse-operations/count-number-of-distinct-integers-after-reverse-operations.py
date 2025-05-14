class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            val=str(nums[i])[::-1]
            nums.append(int(val))
        return len(set(nums))