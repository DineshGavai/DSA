class Solution:
    def minLength(self, s: str) -> int:
        temp=[s[0]]
        for i in range(1,len(s)):
            temp.append(s[i])
            if len(temp)>=2 and (temp[-2]+temp[-1] == "AB" or temp[-2]+temp[-1] == "CD"):
                temp.pop()
                temp.pop()
        return len(temp)

            
            