class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def helper(i,arr,n,k,ds=[]):
            
            if i >= n:                
                if k==0:
                    res.append(ds.copy())
                return
            if arr[i] <= k:
                ds.append(arr[i])
                helper(i,arr,n,k-arr[i],ds)
                ds.pop()
             
            helper(i+1,arr,n,k,ds)
            
            
        n=len(candidates)
        helper(0,candidates,n,target)
        return res
            