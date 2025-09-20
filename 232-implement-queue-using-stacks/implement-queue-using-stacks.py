from collections import deque

class MyQueue:

    def __init__(self):
        self.dq1 = deque()
        self.dq2 = deque()
        # self.currDq = dq1
        # self.emptyDq = dq2

    def push(self, x: int) -> None:
        
        # Move contents out of the way
        while self.dq1:
            self.dq2.append(self.dq1.pop())
        
        # Add new element to the back of the "queue"
        self.dq1.append(x)
        
        # Move contents back into place
        while self.dq2:
            self.dq1.append(self.dq2.pop())

    def pop(self) -> int:
        return self.dq1.pop()

    def peek(self) -> int:
        top = self.dq1.pop()
        self.dq1.append(top)
        return top

    def empty(self) -> bool:
        return (len(self.dq1) == 0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()