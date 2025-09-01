from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        if grid[0][0]==1:
            return -1
        distance=[[-1 for _ in range(col)]for _ in range(row)]
        pq=deque()
        pq.append((1,0,0))
        distance[0][0]=1
        locations=[(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

        while pq:
            dist,i,j=pq.popleft()
            for dx,dy in locations:
                new_x,new_y=i+dx,j+dy
                if new_x < 0 or new_x==row or new_y < 0 or new_y==col:
                    continue
                if distance[new_x][new_y]!=-1  or grid[new_x][new_y]==1:
                    continue
                distance[new_x][new_y]=dist+1
                pq.append((dist+1,new_x,new_y))
        return distance[row-1][col-1]


