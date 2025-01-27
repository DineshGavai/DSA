class Solution:
    def minElement(self, nums: List[int]) -> int:
        res=[]
        for i in nums:
            temp=0
            while i > 0:
                temp+=i%10
                i//=10
            res.append(temp)
        return min(res)