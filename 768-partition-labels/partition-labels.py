class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res=[]
        l = [0] * 26
        for i in range(len(s)):
            idx = ord(s[i]) - ord("a")
            l[idx] = i

        i = 0
        start=0
        end=0
        while i < len(s):
            end=max(end,l[ord(s[i])-ord('a')])
            if i == end:
                res.append(end-start+1)
                start=end+1
            i+=1
        return res