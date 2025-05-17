class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            remaining_val=target-nums[i]
            if remaining_val in d:
                return [i,d[remaining_val]]
            d[nums[i]]=i