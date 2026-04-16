class MinStack:

    def __init__(self):
        # we create the empty stack here
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # push using append
        self.stack.append(val)
        # if min_stack is empty push the val into it
        # if val < min_stack[-1] push to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # if we are popping min value, 
        # pop from the min_stack as well
        # pop using built in pop
        if self.min_stack[-1] == self.stack.pop():
            self.min_stack.pop()

    def top(self) -> int:
        # return top element
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
