from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(set(word)) < 9:
            return len(word)
        freq=Counter(word)
        freq=sorted(freq.values(),reverse=True)
        count=0    
        for i , j in enumerate(freq):
            count+=(i//8+1)*j

    
        return count
        
        
        