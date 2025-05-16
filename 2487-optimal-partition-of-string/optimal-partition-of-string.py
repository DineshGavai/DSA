class Solution:
    def partitionString(self, s: str) -> int:
        if len(set(s))==len(s):
            return 1
        res=1
        temp=""
        for i in range(len(s)):
            if s[i] not in temp:
                temp+=s[i]
            else:
                res+=1
                temp=s[i]


        return res