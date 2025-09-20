class MinStack:

    def __init__(self):
        self.stack = []
        self.minElement = 2 ** 31
        self.lastIndex = -1
        self.minHistory = [] # Used to keep track of previous mins for when the min gets removed

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minElement: # Using leq specifically allows duplicate mins to guard their minimality
            self.minHistory.append(self.minElement) # Store previous min in case new one gets thrown out
            self.minElement = val

    def pop(self) -> None:
        toPop = self.stack[self.lastIndex]
        if toPop == self.minElement:
            self.minElement = self.minHistory.pop() # Revert to previous min

        self.stack.pop()

    def top(self) -> int:
        return self.stack[self.lastIndex]
        

    def getMin(self) -> int:
        return self.minElement


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()