class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if (r < 0 or c < 0 or
                r==Rows or c==Cols or
                grid[r][c]==0 or (r,c) in visited
            ):
                return 0
            visited.add((r,c))
            res=grid[r][c]
            neighbors=[[r+1,c],[r,c+1],[r-1,c],[r,c-1]]
            for nr,nc in neighbors:
                res+=dfs(nr,nc)
            return res

        Rows,Cols=len(grid),len(grid[0])
        res=0
        visited=set()
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c]and (r,c) not in visited:
                    res=max(res,dfs(r,c))
        return res

