class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        cumm_arr=[0]*len(nums)
        for i,j in queries:
            cumm_arr[i]+=1
            if j+1 < len(nums):
                cumm_arr[j+1]-=1
        res=[0]*len(nums)
        for i in range(len(cumm_arr)):
            res[i]+=res[i-1]+cumm_arr[i]
        
        for i in range(len(nums)):
            if res[i] < nums[i]:
                return False
        return True 
        

        