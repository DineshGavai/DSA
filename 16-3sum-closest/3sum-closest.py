class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closest_sum=float('inf')
        for i in range(n):
            j=i+1
            k=n-1
            while j  < k:
                total=nums[i]+nums[j]+nums[k]
                
                if abs(target-total) < abs(target-closest_sum):
                    closest_sum=total
                if total < target:
                    j+=1
                elif total > target:
                    k-=1
                else:
                    # exact match found
                    return total

        return closest_sum

