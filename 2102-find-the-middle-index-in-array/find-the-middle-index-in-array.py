class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            first_half=nums[:i+1]
            second_half=nums[i:]
            print("first Half:",first_half," second Half: ",second_half, "at index: ",i)
            if sum(first_half)==sum(second_half):
                return i
        return -1