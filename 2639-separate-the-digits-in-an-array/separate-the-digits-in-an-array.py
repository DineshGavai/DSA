class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            word=str(i)
            for j in range(len(word)):
                res.append(int(word[j]))
            
        return res
