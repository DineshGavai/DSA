class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i=0
        d=len(s)
        res=[]
        for j in s:
            if j=="I":
                res.append(i)
                i+=1
            else :
                res.append(d)
                d-=1
        res.append(i)
        return res