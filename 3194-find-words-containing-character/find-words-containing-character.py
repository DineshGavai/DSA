class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res=[]
        for word in range(len(words)):
            idx=words[word].find(x)
            if idx != -1:
                res.append(word)
        return res