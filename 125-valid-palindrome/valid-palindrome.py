class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for i in s:
            if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z") or  (i >= "0" and i <= "9"):
                string+=i.lower()
        i,j=0,len(string)-1
        while j >= i:
            if string[i]!=string[j]:
                return False
            i+=1
            j-=1
        return True