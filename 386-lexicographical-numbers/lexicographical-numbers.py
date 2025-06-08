class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr=[]
        for i in range(1,n+1):
            arr.append(str(i))
        
        arr.sort()
        res=[]
        for i in arr:
            res.append(int(i))
        return res