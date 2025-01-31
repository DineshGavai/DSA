class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def inBounds(r: int, c: int) -> bool:
            return 0 <= r < n and 0 <= c < n
        
        def getNeighbors(r: int, c: int) -> List[tuple]:
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            return [(r + dr, c + dc) for dr, dc in directions if inBounds(r + dr, c + dc)]
        
        # DFS to mark each island with a unique ID and return its size
        def markIsland(r: int, c: int, islandId: int) -> int:
            if not inBounds(r, c) or grid[r][c] != 1:
                return 0
                
            grid[r][c] = islandId
            size = 1
            
            for nr, nc in getNeighbors(r, c):
                if grid[nr][nc] == 1:
                    size += markIsland(nr, nc, islandId)
            
            return size
        
        # First pass: mark all islands with unique IDs starting from 2
        # (since 0 and 1 are used in the input grid)
        islandSizes = {0: 0}  # Initialize with 0 to handle cells that can't be connected
        nextIslandId = 2
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = markIsland(r, c, nextIslandId)
                    islandSizes[nextIslandId] = size
                    nextIslandId += 1
        
        # If there are no islands, changing any 0 to 1 would create an island of size 1
        if len(islandSizes) == 1:
            return 1 if any(0 in row for row in grid) else n * n
        
        # Second pass: try to connect islands through each 0 cell
        maxSize = max(islandSizes.values())  # Initialize with largest existing island
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    # Get unique IDs of adjacent islands
                    neighborIds = {grid[nr][nc] for nr, nc in getNeighbors(r, c)}
                    # Calculate total size after connecting
                    totalSize = 1 + sum(islandSizes[id] for id in neighborIds)
                    maxSize = max(maxSize, totalSize)
        
        return maxSize