class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        el=0
        for i in range(len(nums)):
            if cnt == 0:
                cnt=1
                el=nums[i]
            elif el == nums[i]:
                cnt+=1
            else:
                cnt-=1
        cnt1=0
        for i in range(len(nums)):
            if nums[i] == el:
                cnt+=1
        if cnt > len(nums)//2:
            return el