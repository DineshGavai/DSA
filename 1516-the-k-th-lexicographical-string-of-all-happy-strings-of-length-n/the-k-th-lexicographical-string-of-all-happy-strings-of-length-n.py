class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(current):
            if len(current) == n:
                happy_strings.append("".join(current))
                return
            
            for ch in "abc":
                if not current or current[-1] != ch:  # Ensure no consecutive chars are the same
                    backtrack(current + [ch])
        
        happy_strings = []
        backtrack([])
        
        return happy_strings[k - 1] if k <= len(happy_strings) else ""