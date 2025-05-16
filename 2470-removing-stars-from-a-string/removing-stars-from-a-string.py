class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i in s:
            if i=="*":
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)



        # star_count=s.count("*")
        # s=list(s)
        # for i in range(star_count):
        #     idx=s.index("*")
        #     del s[idx-1:idx+1]
        # return "".join(s)