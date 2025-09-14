class Solution:
    def func(self,i,j,triangle,n,dp):
        if dp[i][j]!=-1:
            return dp[i][j]
        if i==n-1:
            dp[i][j]=triangle[i][j]
            return triangle[i][j]
        
        down=triangle[i][j]+self.func(i+1,j,triangle,n,dp)
        diagonal=triangle[i][j]+self.func(i+1,j+1,triangle,n,dp)
        dp[i][j]=min(down,diagonal)
        return dp[i][j]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[-1 for _ in range(n)]for _ in range(n)]
        for j in range(0,n):
            dp[n-1][j]=triangle[n-1][j]
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                down=triangle[i][j]+dp[i+1][j]
                diagonal=triangle[i][j]+dp[i+1][j+1]
                dp[i][j]=min(down,diagonal)
        return dp[0][0]