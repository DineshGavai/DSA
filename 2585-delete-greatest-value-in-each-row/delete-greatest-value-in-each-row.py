class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for col in grid:
            col.sort(reverse=True)
        res=0
        for col in range(len(grid[0])):
            col_max=0
            for row in range(len(grid)):
                col_max = max(col_max, grid[row][col])
            res += col_max
        return res