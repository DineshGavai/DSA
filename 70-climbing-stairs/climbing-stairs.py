class Solution:
    def climbStairs(self, n: int) -> int:

        a=1
        b=2
        for i in range(2,n+1):
            a,b=b,b+a
        return a
