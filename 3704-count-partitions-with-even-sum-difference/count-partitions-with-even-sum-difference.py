class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        res=0
        total=sum(nums)
        first=nums[0]
        second=total-nums[0]
        for i in range(1,len(nums)):
            diff=first-second
            if diff % 2 == 0:
                res+=1
            first+=nums[i]
            second-=nums[i]

        return res



