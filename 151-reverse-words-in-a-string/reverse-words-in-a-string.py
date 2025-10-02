class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split(" ")
        while "" in l:
            l.remove("")
        print(l)
        l.reverse()
        return " ".join(l)