class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res=[]
        l = [0] * 26
        for i in range(len(s)):
            idx = ord(s[i]) - ord("a")
            l[idx] = i

        i = 0
        while i < len(s):
            end = l[ord(s[i])-ord('a')]
            j = i
            while j < end:
                end = max(end, l[ord(s[j])-ord('a')])
                j += 1
            res.append(j-i+1)
            i=j+1
        return res