class Solution:
    def minimumDeletions(self, s: str) -> int:
        res=0
        stack=[]
        for i in s:
            if len(stack)==0 or stack[-1]=="a":
                stack.append(i)
            elif stack[-1]=="b" and i=="b":
                stack.append(i)
            else:
                stack.pop()
                res+=1
        return res
