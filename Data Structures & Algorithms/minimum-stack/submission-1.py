class MinStack:

    def __init__(self):
        # we create the empty stack here
        self.stack = []

    def push(self, val: int) -> None:
        # push using append
        self.stack.append(val)

    def pop(self) -> None:
        # pop using built in pop
        self.stack.pop()

    def top(self) -> int:
        # return top element
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
