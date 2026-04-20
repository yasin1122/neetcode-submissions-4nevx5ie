class Node:
    def __init__(self, val = 0):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        # initialize dummy head and tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail          

    def append(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        new_node.prev = self.head
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        result = self.tail.prev
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        return result.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        result = self.head.next
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        return result.val
