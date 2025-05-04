class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            first_half=nums[:i]
            second_half=nums[i+1:]
            if sum(first_half)==sum(second_half):
                return i
        return -1