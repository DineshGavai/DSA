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
        
        for i in range(len(even)):
            res.append(even[i])
            res.append(odd[i])

        return res
            