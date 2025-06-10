class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=sorted(set(nums))
        res=1
        temp=1
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                temp+=1
                res=max(res,temp)
            else:
                temp=1

        return res