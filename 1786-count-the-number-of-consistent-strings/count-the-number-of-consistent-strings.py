class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in words:
            flag=False
            for j in i:
                if j in allowed :
                    flag=True
                else:
                    flag=False
                    break
            if flag:
                count+=1
                
                             
        return count