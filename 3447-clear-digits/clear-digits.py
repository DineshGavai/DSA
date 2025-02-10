class Solution:
    def clearDigits(self, s: str) -> str:
        arr=[]
        for i in range(len(s)):
            if s[i].isdigit():
                arr.pop()
            else:
                arr.append(s[i])
        return "".join(arr)