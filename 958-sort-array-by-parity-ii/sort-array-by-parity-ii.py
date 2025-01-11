class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        even=[]
        odd=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        
        for i in range(n):
            if i%2==0:
                res.append(even.pop())
            else:
                res.append(odd.pop())
        return res
            