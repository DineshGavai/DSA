class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num=min(nums)
        max_num=max(nums)
        res=0
        for i in range(1,min_num+1):
            if min_num%i==0 and max_num%i==0:
                res=i
        return res