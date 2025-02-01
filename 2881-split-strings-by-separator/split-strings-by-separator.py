class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        temp=[]
        for i in words:
            temp+=i.split(separator)
        res=[]
        for i in temp:
            if i != "":
                res.append(i)
        return res