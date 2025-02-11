class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        res=0
        temp=0
        for i in range(len(grid)):
            a=grid[i].count(1)
            if a > temp:
                temp=a
                res=i
        return res