class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res=[True]*len(l)
        for i in range(len(l)):
            temp=nums[l[i]:r[i]+1]
            temp.sort(reverse=True)
            diff=temp[1]-temp[0]
            for j in range(1,len(temp)-1):
                if temp[j+1]-temp[j]!=diff:
                    res[i]=False
                    break
                else:
                    res[i]=True
        return res