class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        one_row=[]
        one_col=[]
        zero_row=[]
        zero_col=[]
        m,n=len(grid),len(grid[0])
        for i in range(m):
            one_row.append(grid[i].count(1))
            zero_row.append(grid[i].count(0))
        for j in range(n):
            temp=[]
            for i in range(m):
                temp.append(grid[i][j])
            
            one_col.append(temp.count(1))
            zero_col.append(temp.count(0))
        res=[]
        for i in range(m):
            temp=[]
            for j in range(n):
                val=one_row[i]+one_col[j]-zero_row[i]-zero_col[j]
                temp.append(val)
            res.append(temp)
        return res



            
