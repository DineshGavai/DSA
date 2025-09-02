import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row=len(heights)
        col=len(heights[0])

        efforts=[[float('inf')for _ in range(col) ]for _ in range(row)]
        efforts[0][0]=0
        pq=[(0,0,0)]
        locations=[(-1,0),(0,-1),(1,0),(0,1)]
        while pq:
            eff,i,j=heapq.heappop(pq)
            if i==row-1 and j==col-1:
                return eff 
            for dx,dy in locations:
                new_i=i+dx
                new_j=j+dy
                if new_i < 0 or new_i==row or new_j < 0 or new_j==col:
                    continue
                new_eff=max(eff,abs(heights[i][j]-heights[new_i][new_j]))
                if new_eff < efforts[new_i][new_j]:
                    efforts[new_i][new_j]=new_eff
                    heapq.heappush(pq,(new_eff,new_i,new_j))

