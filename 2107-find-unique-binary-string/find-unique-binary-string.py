class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length=len(nums[0])
        bin_set=list()
        for i in range(2**length):
            binary = format(i, f'0{length}b')
            if binary not in nums:
                return binary
        
