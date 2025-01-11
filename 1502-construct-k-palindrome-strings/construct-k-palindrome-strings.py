class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        count_s=Counter(s)
        odd=0
        for cnt in count_s.values():
            odd+=cnt%2
        
        if odd > k :
            return False
        return True