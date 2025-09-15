class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res=0
        text=text.split(" ")
        broken=set(brokenLetters)
        for i in text:
            can_type=True
            for j in broken:
                if j in i:
                    can_type=False
            if can_type:
                res+=1
        return res


                    