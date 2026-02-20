class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left_max=[height[0]]
        right_max=[height[n-1]]*n
        for i in range(1,n):
            curr=max(left_max[-1],height[i])
            left_max.append(curr)
        
        for i in range(n-2,-1,-1):
            curr=max(height[i],right_max[i+1])
            right_max[i]=curr

        print(left_max)
        print(right_max)
        
        res=0
        for i in range(n):
            curr=min(left_max[i],right_max[i])
            water=curr-height[i]
            res+=water
        return res