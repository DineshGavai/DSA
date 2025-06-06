class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        cnt = len(set(nums))
        res=0
        for i in range(n):
            freq=set()
            for j in range(i,n):
                freq.add(nums[j])

                if len(freq) == cnt:
                    res+=1
        return res





