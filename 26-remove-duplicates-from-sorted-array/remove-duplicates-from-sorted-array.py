class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,1
        n=len(nums)
        while j < n:
            if nums[i]!= nums[j]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
            

        return i+1
