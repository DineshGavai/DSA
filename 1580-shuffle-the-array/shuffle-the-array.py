class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[]
        i=0
        j=n
        while(i < n):
            res.append(nums[i])
            res.append(nums[j])
            i+=1
            j+=1
        return res
        