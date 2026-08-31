class Node:
    def __init__(self, val = -1):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def getPrev(self, index: int) -> Node:
        curr = None
        if index <= self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index + 1):
                curr = curr.prev
        return curr

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self.getPrev(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                new_node = Node(val)
                curr.prev.next = new_node
                new_node.prev = curr.prev
                new_node.next = curr
                curr.prev = new_node
                self.size += 1
                return
            curr = curr.next
            i += 1

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        i = 0
        while curr.next:
            if i == index:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                self.size -= 1
                return
            curr = curr.next
            i += 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)