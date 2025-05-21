class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=[0]*len(matrix)
        col=[0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        for i in range(len(matrix)):
            if row[i]==1:
                for j in range(len(matrix[0])):
                    matrix[i][j]=0
        for i in range(len(matrix[0])):
            if col[i]==1:
                for j in range(len(matrix)):
                    matrix[j][i]=0
                
        
        
                
