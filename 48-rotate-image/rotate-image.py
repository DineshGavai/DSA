class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)-1):
            for j in range(i+1,len(matrix[0])):
                if i==j:
                    continue
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]

        for arr in matrix:
            arr.reverse()