class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        intersect_set=set(nums[0])
        for i in range(1,len(nums)):
            intersect_set&=set(nums[i])
        return sorted(intersect_set)
        