class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        double=set()
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                double.add(nums[i])
        res=0
        if not double:
            return res
        else:
            for i in double:
                res^=i

        return res