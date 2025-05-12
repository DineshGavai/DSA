class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        l=[i for i in range(1,n+1)]
        i=0
        while len(l) > 1:
            idx=(i+k-1)%len(l)
            l.pop(idx)
            i=idx
        return l[0]
       
       
       
       
       
       
       
       
       
       
       
       
       
        # start=k
        # for i in range(n):
        #     if start > len(l):
        #         start=start%k
        #     start=start%n
        #     print(start)
        #     l.pop(start-1)
        #     start+=k
        # return l[start-1]