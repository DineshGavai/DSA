class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index_map = {num: i for i, num in enumerate(arr)}  # Map number to its index
        dp = defaultdict(lambda: 2)  # Default length is 2 for any pair (i, j)
        max_length = 0
    
        # Iterate through all pairs (i, j)
        for j in range(len(arr)):
            for i in range(j):
                expected = arr[j] - arr[i]  # Find the previous Fibonacci number
                if expected in index_map and index_map[expected] < i:
                    k = index_map[expected]
                    dp[i, j] = dp[k, i] + 1  # Extend the Fibonacci sequence
                    max_length = max(max_length, dp[i, j])
    
        return max_length if max_length >= 3 else 0  
    