class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        parity=""
        if nums[0]%2==0:
            parity="even"
        else:
            parity="odd"
        for i in range(1,len(nums)):
            
            if nums[i]%2==0 and parity=="even":
                return False
            elif nums[i]%2==1 and parity=="odd":
                return False
            if nums[i]%2==0:
                parity="even"
            else:
                parity="odd"
        return True
            

            