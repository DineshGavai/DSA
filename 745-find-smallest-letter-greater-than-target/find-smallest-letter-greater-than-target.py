class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target > letters[-1]:
            return letters[0]
        if target == letters[-1]:
            return letters[0]
            
        for i in letters:
            if i > target:
                return i
        
        
        
        
        
        
        
        
        
        
        
        
        
        # target_value=ord(target)
        # n=len(letters)
        # if ord(letters[0]) > target_value:
        #         return letters[0]
        
        # elif ord(letters[n-1]) < target_value :
        #         return letters[0]
        
        # for i in range(len(letters)-1):
        #     if ord(letters[i]) == target_value:
        #         if i==n-1:
        #             return letters[0]
        #         else:
        #             return letters[i+1]
        #     elif ord(letters[i]) < target_value and ord(letters[i+1]) > target_value:
        #         return letters[i+1]
            
            