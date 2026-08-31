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

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr.next:
            curr = curr.next
            if i == index:
                return curr.val
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        self.head.next.prev = new_node
        new_node.next = self.head.next
        self.head.next = new_node
        new_node.prev = self.head

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.prev.next = new_node
        new_node.prev = self.tail.prev
        self.tail.prev = new_node
        new_node.next = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        i = 0
        while curr.next:
            curr = curr.next
            if i == index:
                new_node = Node(val)
                curr.prev.next = new_node
                new_node.prev = curr.prev
                new_node.next = curr
                curr.prev = new_node
                return
            i += 1

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        i = 0
        while curr.next.next:
            curr = curr.next
            if i == index:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                return
            i += 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)