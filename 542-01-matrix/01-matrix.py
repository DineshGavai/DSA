from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
        visited=[[0 for _ in range(cols)] for _ in range(rows)]
        distance=[[0 for _ in range(cols)] for _ in range(rows)]
        q=deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    q.append([i,j,0])
                    visited[i][j]=1
        while q:
            i,j,d=q.popleft()
            distance[i][j]=d
            for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_i=i+dx
                new_j=j+dy
                if new_i < 0 or new_i==rows or new_j < 0 or new_j==cols:
                    continue
                if visited[new_i][new_j]==1:
                    continue
                q.append([new_i,new_j,d+1])
                visited[new_i][new_j]=1
        return distance



        
                        
