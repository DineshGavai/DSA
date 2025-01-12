class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sett=set()
        n=len(nums)
        res=[]
        for i in range(n):
            if nums[i] not in sett:
                sett.add(nums[i])
            else:
                res.append(nums[i])

        return res