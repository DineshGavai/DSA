class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=[]
        y=[]
        res=[]
        for i in range(len(nums)):
            if i <n:
                x.append(nums[i])
            else:
                y.append(nums[i])
        for i in range(n):
            res.append(x[i])
            res.append(y[i])
        return res
