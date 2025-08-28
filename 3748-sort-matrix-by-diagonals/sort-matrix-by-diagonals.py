class Solution:
    def sortDiagonal(self,row,col,grid,ascending):
        arr=[]
        i , j =row , col
        while i < len(grid) and j < len(grid[0]):
            arr.append(grid[i][j])
            i+=1
            j+=1
        if ascending:
            arr.sort(reverse=True)
        else:
            arr.sort()
        i , j =row , col
        while i < len(grid) and j < len(grid[0]):
            grid[i][j]=arr.pop()
            i+=1
            j+=1

    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        for row in range(n):
            self.sortDiagonal(row,0,grid,ascending=False)
        m=len(grid[0])
        for col in range(1,m):
            self.sortDiagonal(0,col,grid,ascending=True)
        return grid


