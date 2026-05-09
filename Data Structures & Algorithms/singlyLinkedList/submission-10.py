class Node:

    def __init__(self, val = -1, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node()
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next, self.head.next = self.head.next, new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        # new_node = Node(val)
        self.tail.next = self.tail = Node(val)
        # self.tail = new_node

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while curr and curr.next:
            if i == index:
                if curr.next == self.tail:
                    self.tail = curr
                curr.next = curr.next.next
                return True
            i += 1
            curr = curr.next
        return False

    def getValues(self) -> List[int]:
        result = []
        curr = self.head.next

        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
        
