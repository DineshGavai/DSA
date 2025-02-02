import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets=list(string.ascii_lowercase)
        for i in alphabets:
            if i not in sentence:
                return False
        return True