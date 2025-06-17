class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def helper(total):
            if total == target:
                return 1
            if total > target:
                return 0
            if total in memo:
                return memo[total]

            count = 0
            for num in nums:
                count += helper(total + num)

            memo[total] = count
            return count

        return helper(0)

        

