class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res,sol=[],[]
        def backtracking():
            if len(sol)==n:
                res.append(sol[:])
                return
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtracking()
                    sol.pop()
        backtracking()

        return res
