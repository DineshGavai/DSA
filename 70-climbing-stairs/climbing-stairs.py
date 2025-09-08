class Solution:
    def climbStairs(self, n: int) -> int:

        def func(n,memo={}):
            if n in memo:
                return memo[n]
            if n==1 or n==0:
                return 1
            memo[n]=func(n-1,memo)+func(n-2,memo)
            return memo[n]

        return func(n)