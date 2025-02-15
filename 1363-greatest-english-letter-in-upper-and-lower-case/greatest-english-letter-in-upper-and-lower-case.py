class Solution:
    def greatestLetter(self, s: str) -> str:
        temp=set()
        for i in range(len(s)-1):
            if s[i].islower():
                if s[i].upper() in s[i+1:]:
                    temp.add(s[i].upper())
            else:
                if s[i].lower() in s[i+1:]:
                    temp.add(s[i].upper())
        return max(temp) if temp else ""