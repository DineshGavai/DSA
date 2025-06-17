class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums=[1,2,3,4,5,6,7,8,9]
        res=[]
        def helper(start,n,total,arr):
            if total > n:
                return 
            if total==n and len(arr)==k:
                res.append(arr.copy())
                return
            for i in range(start,len(nums)):
                arr.append(nums[i])
                total+=nums[i]
                helper(i+1,n,total,arr)
                total-=arr.pop()
                # helper(i+1,n,total,arr)
        helper(0,n,0,[])
        return res
