class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth=0
        stack=[]
        for i in s:
            if i == "(":
                stack.append(i)
                max_depth=max(max_depth,len(stack))
            elif i == ")":
                stack.pop()
        return max_depth