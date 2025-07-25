class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def backtracking(start,path,total):
            if total==target:
                res.append(path.copy())
                return
            if total > target:
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtracking(i+1,path,total+candidates[i])
                path.pop()
        backtracking(0,[],0)
        return res