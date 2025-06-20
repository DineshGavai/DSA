class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        left,right=0,0
        g.sort()
        s.sort()
        count=0
        while left < len(g) and right < len(s):
            if g[left] <= s[right]:
                count+=1
                left+=1

            right+=1
        return count
            

            