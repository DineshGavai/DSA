class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        temp=[]
        for i in range(len(nums)//2):
            x=nums.pop(0)
            y=nums.pop(-1)
            z=str(x)+str(y)
            temp.append(int(z))
        if nums:
            temp+=nums
        
        return sum(temp)