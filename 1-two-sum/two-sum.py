class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            remain=target-nums[i]
            if remain in hashmap:
                return [i,hashmap[remain]]
            hashmap[nums[i]]=i
            