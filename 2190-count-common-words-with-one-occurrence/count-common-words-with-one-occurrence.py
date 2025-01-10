class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        countA=Counter(words1)
        countB=Counter(words2)
        count=0
        for i ,j in countA.items():
            if countB[i]== 1 and countA[i]==1:
                count+=1
        return count