class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        target=""
        for word in words:
            target+=word[0]
        return target==s
        