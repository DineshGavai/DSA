class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        letters=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res=[]

        def helper(index,subset):
            if index >= len(digits):
                res.append(''.join(subset))
                return

            for ch in letters[int(digits[index])-2]:
                 subset.append(ch)
                 helper(index+1,subset)
                 subset.pop()
        helper(0,[])
        return res
                



