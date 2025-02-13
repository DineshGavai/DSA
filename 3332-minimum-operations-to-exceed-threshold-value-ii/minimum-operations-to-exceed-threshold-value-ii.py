from heapq import heapify, heappop, heappush
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res=0
        heapify(nums)
        while nums[0] < k:
            x=heappop(nums)
            y=heappop(nums)

            z=(min(x,y)*2)+max(x,y)
            heappush(nums,z)
            res+=1
        return res
        
        
        
        
        # res=0
        # nums.sort()
        # while nums[0] < k:
        #     x=nums[0]
        #     y=nums[1]
        #     nums.remove(x)
        #     nums.remove(y)
        #     nums.append((min(x,y)*2)+max(x,y))
        #     nums.sort()
        #     res+=1
        # return res

