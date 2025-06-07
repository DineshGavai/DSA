class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=0
        for i in range(len(digits)):
            res=(res*10)+digits[i]
        res=res+1
        res=str(res)
        res_arr=[]
        for i in range(len(res)):
            res_arr.append(int(res[i]))
        return res_arr

        
