import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha=list(string.ascii_lowercase)
        def helper(word):
            morse_code=""
            for i in word:
                idx=alpha.index(i)
                morse_code+=morse[idx]
            return morse_code
        morse_codes=set()
        for i in words:
            word=helper(i)
            morse_codes.add(word)
        return len(morse_codes)
            