class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left_max=[height[0]]
        right_max=[height[n-1]]*n
        # for left max height
        for i in range(1,n):
            maxx=max(left_max[-1],height[i])
            left_max.append(maxx)
        
        # for right max height
        for i in range(n-2,-1,-1):
            maxx=max(height[i],right_max[i+1])
            right_max[i]=maxx
        
        # calculating the water stored
        res=0
        for i in range(n):
            min_height=min(left_max[i],right_max[i])
            water=min_height-height[i]
            res+=water
        return res

