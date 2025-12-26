class Solution:
    def canJump(self, nums: List[int]) -> bool:
        g=len(nums)-1
        step=1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] >= step:
                g-=step
                step=1
            else:
                step+=1
            print(g)

        return g<=0
            