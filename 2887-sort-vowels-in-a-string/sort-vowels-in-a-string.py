class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        def is_vowel(s):
            if s in vowels:
                return True
            return False
        vowel=sorted([ i for i in s if is_vowel(i)])
        s=list(s)
        for i in range(len(s)):
            if is_vowel(s[i]):
                s[i]=vowel.pop(0)
        return "".join(s)