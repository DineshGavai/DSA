from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=[[0 for _ in range(cols)]for _ in range(rows)]
        q=deque()
        res=0
        for r in range(rows):
            for c in range(cols):
                if r==0 or c==0 or r==rows-1 or c==cols-1:
                    if grid[r][c]==1:
                        q.append([r,c])
                        visited[r][c]=1
        while q:
            r,c = q.popleft()
            for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_r,new_c=r+dx,c+dy
                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                    continue
                if grid[new_r][new_c]==1 and visited[new_r][new_c]==0:
                    q.append([new_r,new_c])
                    visited[new_r][new_c]=1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and visited[r][c]==0:
                    res+=1
        return res
