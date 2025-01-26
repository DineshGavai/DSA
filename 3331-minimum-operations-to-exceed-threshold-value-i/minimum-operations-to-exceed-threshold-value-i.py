class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        # for i in range(len(nums)):
        while nums[0] < k:
            nums.pop(0)
            i+=1
        return i
