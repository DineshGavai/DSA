class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
    
        vowels = set("aeiouAEIOU")
        has_vowel = False
        has_consonant = False
    
        for ch in word:
            if ch.isdigit() or ch.isalpha():
                if ch.isalpha():
                    if ch in vowels:
                        has_vowel = True
                    else:
                        has_consonant = True
            else:
                return False  
    
        return has_vowel and has_consonant