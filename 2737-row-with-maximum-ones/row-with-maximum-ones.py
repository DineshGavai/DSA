class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        dict1={}
        for i in range(len(mat)):
            count=0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    count+=1
            dict1[i]=count


        res=[0,0]
        for i,val in dict1.items():
            if val > res[-1]:
                res[0]=i
                res[1]=val
        return res
