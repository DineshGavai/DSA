class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2!=0:
            return False
        half=total//2
        n=len(nums)
        dp=[[-1 for _ in range(half+1)]for _ in range(n)]
        def func(i,target):
            if target == 0:
                return True
            if i == 0:
                return nums[0] == target
            if dp[i][target] != -1:
                return dp[i][target]
            not_pick = func(i - 1, target)

            pick = False
            if nums[i] <= target:
                pick = func(i - 1, target - nums[i])

            dp[i][target]=pick or not_pick
            return dp[i][target]
        return func(n-1,half)
