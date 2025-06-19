class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            stack.append(nums[i])


        for i in range(n-1,-1,-1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            
            if stack:
                res[i]=stack[-1]

            stack.append(nums[i])
        return res
        

