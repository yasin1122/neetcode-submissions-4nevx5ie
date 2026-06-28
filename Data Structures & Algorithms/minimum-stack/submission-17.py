from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.getMin():
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.getMin():
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
