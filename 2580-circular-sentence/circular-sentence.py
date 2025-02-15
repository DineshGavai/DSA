class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        seprated=sentence.split()
        if len(seprated)==1:
            if seprated[0][0]==seprated[0][-1]:
                return True
            else:
                return False
        nulla=0
        first=seprated[0][0]
        for i in range(1,len(seprated)):
            if seprated[i-1][-1]==seprated[i][0]:
                nulla+=1
            else:
                break
        if first==seprated[-1][-1]:
            nulla+=1
        return True if nulla==len(seprated) else False