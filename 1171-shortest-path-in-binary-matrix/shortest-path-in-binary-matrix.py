from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[row-1][col-1] == 1:
            return -1

        # min-heap (distance, x, y)
        pq = [(1, 0, 0)]
        distance = [[float('inf')] * col for _ in range(row)]
        distance[0][0] = 1

        directions = [(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

        while pq:
            dist, i, j = heapq.heappop(pq)

            # Early exit if we reached the target
            if (i, j) == (row-1, col-1):
                return dist

            if dist > distance[i][j]:
                continue  # Skip outdated entry

            for dx, dy in directions:
                new_x, new_y = i + dx, j + dy
                if 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y] == 0:
                    new_dist = dist + 1
                    if new_dist < distance[new_x][new_y]:
                        distance[new_x][new_y] = new_dist
                        heapq.heappush(pq, (new_dist, new_x, new_y))

        return -1


