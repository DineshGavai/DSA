class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        for i in matrix:
            min_val=min(i)
            idx=i.index(min_val)
            flag=False
            for i in range(len(matrix)):
                if matrix[i][idx] > min_val:
                    flag=True
                    break
            if flag==False:
                res.append(min_val)
        return res

            

            