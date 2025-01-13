class Solution:
    def defangIPaddr(self, address: str) -> str:
        res=[]
        for i in address:
            if i == ".":
                res.append("[")
                res.append(".")
                res.append("]")
            else:
                res.append(i)
        return ''.join(res)
