class Solution:
    def partitionString(self, s: str) -> int:
        if len(set(s))==len(s):
            return 1
        res=[]
        temp=""
        for i in range(len(s)):
            if s[i] not in temp:
                temp+=s[i]
            else:
                res.append(temp)
                temp=s[i]


        return len(res)+1