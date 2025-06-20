class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict={}
        l,r=0,0
        max_length=0
        while r < len(s):
            if s[r] in my_dict:
                l=max(l,my_dict[s[r]]+1)
            
            length=r-l+1
            max_length=max(max_length,length)
            my_dict[s[r]]=r
            r+=1

            
        return max_length

            

