class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels=set(["a","e","i","o","u","A","E","I","O","U"])
        def count_vowels(s1):
            count=0
            for i in s1:
                if i in vowels:
                    count+=1
            return count
        n=len(s)//2
        
        return count_vowels(s[:n])==count_vowels(s[n:])