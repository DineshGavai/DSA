class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        n=len(operations)
        for i in range(n):
            if operations[i].lstrip('-').isnumeric():
                res.append(int(operations[i]))
            elif operations[i]=="C":
                res.pop()
            elif operations[i]=="D":
                
                temp=res[-1]*2
                res.append(temp)
            elif operations[i]=="+":
                temp=res[-1]+res[-2]
                res.append(temp)
        print(res)
        return sum(res)


