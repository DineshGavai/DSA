class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res=[]
        temp=""
        for i in range(len(s)):
            temp+=s[i]
            if len(temp) == k :
                res.append(temp)
                temp=""
        last=len(temp)
        if last < k and last > 0:
            req=k-last
            for i in range(req):
                temp+=fill
            res.append(temp)
            
        return res
