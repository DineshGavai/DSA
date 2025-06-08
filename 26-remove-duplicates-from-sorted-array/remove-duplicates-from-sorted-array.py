class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            freq[i]=1

        
        i=0
        for key in freq:
            nums[i]=key
            i+=1
        return len(freq)