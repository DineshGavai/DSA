class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res=0
        for g in grid:
            l=0
            r=len(g)-1
            while l <= r:
                mid=(l+r)//2
                if g[mid] >= 0:
                    l = mid + 1
                else:
                    r = mid - 1
            # print(l)
            res+=len(g[l:])


        return res 
