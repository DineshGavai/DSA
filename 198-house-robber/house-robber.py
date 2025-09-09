class Solution:
    def rob(self, nums: List[int]) -> int:
        def func(idx,memo={}):
            if idx in memo:
                return memo[idx]
            if idx==0:
                return nums[idx]
            if idx < 0:
                return 0
            pick=nums[idx]+func(idx-2)
            not_pick=0+func(idx-1)
            memo[idx]= max(pick,not_pick)
            return memo[idx]

        n=len(nums)
        return func(n-1)