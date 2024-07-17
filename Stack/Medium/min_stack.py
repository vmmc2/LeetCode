class MinStack:
    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
            return
        
        current_minimum = self.stack[-1][1]
        if current_minimum <= val:
            self.stack.append((val, current_minimum))
        else:
            self.stack.append((val, val))
            
        return

    def pop(self) -> None:
        self.stack.pop()

        return

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()