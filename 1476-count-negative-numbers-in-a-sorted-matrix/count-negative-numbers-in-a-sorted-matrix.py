class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res=0
        for i in grid:
            temp=0
            for j in i:
                if j < 0:
                    temp+=1
            res+=temp
        return res 
