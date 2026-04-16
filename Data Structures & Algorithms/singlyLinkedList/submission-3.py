class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next

        while curr:
            if i == index:
                return curr.value
            curr = curr.next
            i += 1
        
        return -1 # index out of bounds

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next: # if the list was empty
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        while curr and i < index:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        
        return False

    def getValues(self) -> List[int]:
        result = []
        curr = self.head.next
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result
