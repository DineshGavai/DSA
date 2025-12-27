class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict=dict()
        i,j=0,0
        n=len(s)
        maxi=0
        while j < n:
            if s[j]  in my_dict:
                i=max(i,my_dict[s[j]]+1)
            maxi=max(maxi,j-i+1)
            my_dict[s[j]]=j
            j+=1   
            
        return maxi   