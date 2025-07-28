class Solution:
    def dfs(self,r,c,rows,cols,grid,visited):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c]== "0":
            return
        if visited[r][c]==1:
            return
        visited[r][c]=1
        self.dfs(r-1,c,rows,cols,grid,visited)
        self.dfs(r,c-1,rows,cols,grid,visited)
        self.dfs(r+1,c,rows,cols,grid,visited)
        self.dfs(r,c+1,rows,cols,grid,visited)


    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=[[0 for _ in range(cols)]for _ in range(rows)]
        res=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]== "1" and visited[r][c]==0:
                    res+=1
                    self.dfs(r,c,rows,cols,grid,visited)
        return res


        