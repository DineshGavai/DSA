class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq=Counter(nums)
        res=0
        for i in nums:
            if freq[i]==1:
                res+=i
        return res