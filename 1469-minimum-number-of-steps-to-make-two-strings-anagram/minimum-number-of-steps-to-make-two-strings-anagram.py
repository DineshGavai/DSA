from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count=0
        freq_s=Counter(s)
        freq_t=Counter(t)
        for key,value in freq_s.items():
            if key not in freq_t:
                count+=value
            elif key in freq_t and value >= freq_t[key]:
                count+=value-freq_t[key]
            
        return count

