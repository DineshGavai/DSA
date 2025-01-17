class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum=[0]
        right_sum=[]
        n=len(nums)
        for i in range(n-1):
            left_sum.append(left_sum[-1]+nums[i])
            right_sum.append(sum(nums[i+1:]))
        right_sum.append(0)
        res=[]
        for i in range(len(left_sum)):
            res.append(abs(left_sum[i]-right_sum[i]))
        return res

