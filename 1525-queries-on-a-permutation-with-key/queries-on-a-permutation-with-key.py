class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p=[i for i in range(1,m+1)]
        res=[]
        for i in range(len(queries)):
            idx=p.index(queries[i])
            popped=p.pop(idx)
            p.insert(0,popped)
            res.append(idx)
            print(p)
        return res

