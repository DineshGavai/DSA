class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        if self.stack:
            last_min=self.stack[-1][-1]
            curr_min=min(val,last_min)
            self.stack.append([val,curr_min])
        else:
            self.stack.append([val,val])
        

    def pop(self) -> None:
        if self.stack:
            x=self.stack.pop()
            return x[0]

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()