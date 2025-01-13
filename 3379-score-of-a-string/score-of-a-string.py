class Solution:
    def scoreOfString(self, s: str) -> int:
        res=0
        for i in range(len(s)-1):
            f_ord=ord(s[i])
            s_ord=ord(s[i+1])
            res+=abs(f_ord-s_ord)
        return res