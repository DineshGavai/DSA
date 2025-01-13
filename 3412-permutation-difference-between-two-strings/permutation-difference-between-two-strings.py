class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res=0
        for i in range(len(s)):
            t_idx=t.find(s[i])
            res+=abs(i-t_idx)
        return res