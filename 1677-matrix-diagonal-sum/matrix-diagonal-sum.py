class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res=0
        n=len(mat)
        m=len(mat[0])
        seen=set()
        for i in range(n):
            res+=mat[i][i]
            seen.add((i,i))
        i=0
        j=m-1
        while i < n and j >= 0:
            if (i,j) not in seen:
                res+=mat[i][j]
            i+=1
            j-=1
        
        
        return res
        
