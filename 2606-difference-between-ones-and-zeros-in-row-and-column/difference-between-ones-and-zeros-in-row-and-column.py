class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        one_row = [0] * len(grid)
        zero_row = [0] * len(grid)
        one_col = [0] * len(grid[0])
        zero_col = [0] * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    one_row[i] += 1
                    one_col[j] += 1
                elif grid[i][j] == 0:
                    zero_row[i] += 1
                    zero_col[j] += 1
        res=[]
        for i in range(len(grid)):
            temp=[]
            for j in range(len(grid[0])):
                val=one_row[i]+one_col[j]-zero_row[i]-zero_col[j]
                temp.append(val)
            res.append(temp)
        return res



            
