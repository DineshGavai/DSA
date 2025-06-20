class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j=0,0
        maxi=0
        n=len(nums)
        zeros=0
        while j < n:
            if nums[j]==0:
                zeros+=1
            while  zeros > k:
                if nums[i]==0:
                    zeros-=1
                i+=1
            if zeros <= k:
                maxi=max(maxi,j-i+1)
            j+=1

        return maxi

