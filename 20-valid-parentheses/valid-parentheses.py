class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        

        for ch in s:
            if ch == '(' or ch == '[' or ch == "{":
                stack.append(ch)
            else:
                if stack:
                    x=stack.pop()
                    if (ch == ')' and x == '(') or (ch == ']' and x == '[') or (ch == '}' and x == '{'):
                        continue
                    else:
                        return False  
                else:
                    return False 
        
        return False if stack else True