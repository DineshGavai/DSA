class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for i in s:
            if i.isalnum():
                string+=i.lower()
        i,j=0,len(string)-1
        while j >= i:
            if string[i]!=string[j]:
                return False
            i+=1
            j-=1
        return True