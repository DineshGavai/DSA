class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res=[]
        for i in range(1,len(A)+1):
            temp_a=A[:i]
            temp_b=B[:i]
            count=0
            for j in temp_a:
                if j in temp_b:
                    count+=1
            res.append(count)

        return res