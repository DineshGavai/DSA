from functools import lru_cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i):
            if i >= n - 1:
                return 0
            min_jumps = float('inf')
            for j in range(1, nums[i] + 1):
                min_jumps = min(min_jumps, 1 + dfs(i + j))
            return min_jumps

        return dfs(0)