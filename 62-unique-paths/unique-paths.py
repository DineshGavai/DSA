from functools import lru_cache
class Solution:
    @lru_cache
    def func(self,i,j,m,n):
        if i==m-1 and j==n-1:
            return 1
        if i >= m or j >= n:
            return 0

        down=self.func(i+1,j,m,n)
        right=self.func(i,j+1,m,n)
        return down+right
    def uniquePaths(self, m: int, n: int) -> int:
        return self.func(0,0,m,n)
       
