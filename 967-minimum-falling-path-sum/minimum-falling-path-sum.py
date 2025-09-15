class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        res=[]
        n=len(matrix)
        dp=[[-1 for _ in range(n)]for _ in range(n)]
        for i in range(n):
            dp[n-1][i]=matrix[n-1][i]
        for i in range(n-2,-1,-1):
            for j in range(n):
                up=matrix[i][j]+dp[i+1][j]
                diagonal_left=matrix[i][j]+(dp[i+1][j-1] if j-1 >= 0 else float('inf'))
                diagonal_right=matrix[i][j]+(dp[i+1][j+1] if j+1 < n else float('inf'))
                dp[i][j]=min(up,diagonal_left,diagonal_right)
        return min(dp[0])
