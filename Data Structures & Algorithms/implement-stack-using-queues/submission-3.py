

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.size += 1

    def pop(self) -> int:
        for _ in range(self.size - 1):
            self.q2.append(self.q1.popleft())
        self.size -= 1
        result = self.q1.popleft()
        while self.q2:
            self.q1.append(self.q2.popleft())
        return result

    def top(self) -> int:
        for _ in range(self.size - 1):
            self.q2.append(self.q1.popleft())
        result = self.q1.popleft()
        self.q2.append(result)
        while self.q2:
            self.q1.append(self.q2.popleft())
        return result

    def empty(self) -> bool:
        return not self.size


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()