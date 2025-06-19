class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        i,j=0,0
        n=len(nums)
        res=0
        # [1,2,3,5,6]
        while i < n:
            if nums[i]-nums[j] <= k:
                i+=1
            else:
                res+=1
                j=i
                i+=1
        res+=1
        return res
            
