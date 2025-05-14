class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]

        def helper(nums,i,temp):
            if i >= len(nums):
                result.append(temp[:])
                return
            temp.append(nums[i])
            helper(nums,i+1,temp)
            temp.pop()
            helper(nums,i+1,temp)
        
        helper(nums,0,[])
        return result