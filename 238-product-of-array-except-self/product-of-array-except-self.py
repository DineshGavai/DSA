class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[]
        right=[1]*n
        last_left=1
        last_right=1
        for i in range(n):
            left.append(last_left)
            last_left*=nums[i]
        for i in range(n-1,-1,-1):
            right[i]=last_right
            last_right*=nums[i]
        res=[]
        for i in range(n):
            res.append(left[i]*right[i])
        return res