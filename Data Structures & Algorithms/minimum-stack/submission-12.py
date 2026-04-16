class MinStack:

    def __init__(self):
        # initialize a stack and a min_stack to retrieve min value
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # push to stack 
        # push to min_stack if val <= min_stack[-1]
        # check if min_stack is empty first
        # <= to collect duplicates
        self.stack.append(val)
        if not self.min_stack or val <= self.getMin():
            self.min_stack.append(val)

    def pop(self) -> None:
        # pop from stack
        # pop from min_stack if popped val = min_stack[-1]
        if self.stack.pop() == self.getMin():
            self.min_stack.pop()

    def top(self) -> int:
        # return stack[-1]
        return self.stack[-1]

    def getMin(self) -> int:
        # return min_stack[-1]
        return self.min_stack[-1]