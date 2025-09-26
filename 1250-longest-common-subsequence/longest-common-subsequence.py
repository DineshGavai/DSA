class Solution:
    def func(self,ind1,ind2,text1,text2,dp):
        if ind1 < 0 or ind2 < 0:
            return 0
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
        if text1[ind1]==text2[ind2]:
            dp[ind1][ind2]= 1 + self.func(ind1-1,ind2-1,text1,text2,dp)
            return dp[ind1][ind2]
        dp[ind1][ind2]= 0 + max(self.func(ind1-1,ind2,text1,text2,dp),self.func(ind1,ind2-1,text1,text2,dp))
        return dp[ind1][ind2]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ind1=len(text1)
        ind2=len(text2)
        dp=[[-1 for _ in range(ind2)]for _ in range(ind1)]
        return self.func(ind1-1,ind2-1,text1,text2,dp)
        