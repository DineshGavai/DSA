class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # nums=list(num)
        # for i in range(len(nums)-1,0,-1):
        #     if nums[i]=="0":
        #         nums.pop()
        #     else:
        #         break
        # return "".join(nums)
        s=num.rstrip('0')
        return s