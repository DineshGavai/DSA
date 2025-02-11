class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq=Counter(nums)
        for i in freq.values():
            if i%2!=0:
                return False
        return True