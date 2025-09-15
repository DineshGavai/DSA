class Solution:
    def func(self,i,j,arr,n,dp):
        if j < 0 or j >= n:
                return float('inf')
        if dp[i][j]!=-1:
            return dp[i][j]
        if i == n - 1:
            return arr[i][j]
     
        down=arr[i][j]+self.func(i+1,j,arr,n,dp)
        diagonal_left=arr[i][j]+self.func(i+1,j-1,arr,n,dp)
        diagonal_right=arr[i][j]+self.func(i+1,j+1,arr,n,dp)
        
        dp[i][j]=min(down,diagonal_left,diagonal_right)
        return dp[i][j]

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


























        # for i in range(n):
        #     res.append(self.func(0,i,matrix,m,dp))
        # return min(res)