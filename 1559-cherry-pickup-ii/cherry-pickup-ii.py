class Solution:
    def func(self,i,j1,j2,grid,dp):
        if j1 < 0 or j1 >= len(grid[0]) or j2 < 0 or j2 >= len(grid[0]):
            return float("-inf")
        if  i==len(grid)-1:
            if j1==j2:
                return grid[i][j1]
            return grid[i][j1]+grid[i][j2]
        if dp[i][j1][j2]!= -1:
            return dp[i][j1][j2]
        maxi=0
        for new_j1 in range(-1,2):
            for new_j2 in range(-1,2):
                if j1==j2:
                    ans=grid[i][j1]+self.func(i+1,j1+new_j1,j2+new_j2,grid,dp)
                else:
                    ans=grid[i][j1]+grid[i][j2]+self.func(i+1,j1+new_j1,j2+new_j2,grid,dp)
                maxi=max(maxi,ans)
        dp[i][j1][j2]=maxi 
        return maxi           
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[[-1 for _ in range(m)]for _ in range(m)]for _ in range(n)]
        return self.func(0,0,m-1,grid,dp)
        
