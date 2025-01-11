class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count_nums=Counter(nums)
        max_elem=max(count_nums,key=count_nums.get)
        return max_elem    