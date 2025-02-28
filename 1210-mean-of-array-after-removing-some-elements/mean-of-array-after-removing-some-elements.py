class Solution:
    def trimMean(self, arr: List[int]) -> float:
        num=(5/100)*len(arr)
        for i in range(int(num)):
            arr.remove(min(arr))
            arr.remove(max(arr))
        return (sum(arr)/len(arr))

        