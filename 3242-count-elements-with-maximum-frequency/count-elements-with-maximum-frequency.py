class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq=Counter(nums)
        max_freq=0
        for idx,val in freq.items():
            max_freq=max(max_freq,val)
        res=0
        for idx,val in freq.items():
            if val==max_freq:
                res+=max_freq
        return res