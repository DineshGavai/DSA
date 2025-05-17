class Solution:
    def isHappy(self, n: int) -> bool:
        temp=n
        hash_set=set()
        while temp != 1:
            
            temp=str(temp)
            k=0
            for i in range(len(temp)):
                k+=int(temp[i])**2
            temp=k
            if temp in hash_set:
                return False
            hash_set.add(temp)
        return True

        
