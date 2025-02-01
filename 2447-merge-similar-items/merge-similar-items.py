class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        merged = defaultdict(int)  # Dictionary to store value → total weight

        # Process items1
        for value, weight in items1:
            merged[value] += weight

        # Process items2
        for value, weight in items2:
            merged[value] += weight

        return sorted([[value, weight] for value, weight in merged.items()])
        

