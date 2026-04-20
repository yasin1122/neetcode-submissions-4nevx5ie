from collections import deque

class Deque:
    
    def __init__(self):
        self.queue = deque()

    def isEmpty(self) -> bool:
        return not self.queue

    def append(self, value: int) -> None:
        self.queue.append(value)

    def appendleft(self, value: int) -> None:
        self.queue.appendleft(value)

    def pop(self) -> int:
        return self.queue.pop() if self.queue else -1

    def popleft(self) -> int:
        return self.queue.popleft() if self.queue else -1

