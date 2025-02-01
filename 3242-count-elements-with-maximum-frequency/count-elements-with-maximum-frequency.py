class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq=Counter(nums)
        max_freq=max(freq.values())
        res=0
        for idx,val in freq.items():
            if val==max_freq:
                res+=max_freq
        return res