class Solution:
    def countKeyChanges(self, s: str) -> int:
        s=list(s)
        print(s)
        res=0
        for i in range(len(s)-1):
            if s[i+1].lower()!=s[i].lower() :
                res+=1
        return res