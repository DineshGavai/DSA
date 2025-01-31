class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq=Counter(arr)
        last=set()
        for idx,val in freq.items():
            if val in last:
                return False
            last.add(val)

        return True