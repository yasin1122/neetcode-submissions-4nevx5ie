class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MiniStack:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def push(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1

    def top(self) -> int:
        return self.tail.prev.val

    def pop(self) -> None:
        if self.size == 0:
            return
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size -= 1

class MinStack(MiniStack):
    def __init__(self):
        super().__init__()
        self.min_stack = MiniStack()

    def push(self, val: int) -> None:
        super().push(val)
        
        # Update the min tracking stack
        if self.min_stack.size == 0 or val <= self.min_stack.top():
            self.min_stack.push(val)

    def pop(self) -> None:
        if self.size == 0:
            return
            
        if self.min_stack.top() == self.top():
            self.min_stack.pop()
            
        super().pop()

    def getMin(self) -> int:
        return self.min_stack.top()


