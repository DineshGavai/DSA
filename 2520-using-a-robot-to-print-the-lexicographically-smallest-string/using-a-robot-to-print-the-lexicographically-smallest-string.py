class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
    
    # Step 1: Precompute the minimum suffix character at each position
        min_suffix = [''] * n
        min_suffix[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])

        t_stack = []
        result = []

        # Step 2: Traverse through s and simulate the process
        for i in range(n):
            t_stack.append(s[i])  # Push to t
            # While we can pop from t to result to get smallest lex result
            while t_stack and (i == n - 1 or t_stack[-1] <= min_suffix[i + 1]):
                result.append(t_stack.pop())

        # Step 3: Add remaining characters in t to result
        while t_stack:
            result.append(t_stack.pop())

        return ''.join(result)  