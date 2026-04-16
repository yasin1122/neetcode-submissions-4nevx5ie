class Node:
    def __init__(self, value):
        # Santinel Node, initialize with value
        # Next points to None
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        # Dummy Node makes edge cases easier
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        # point to the real head (dummy.next)
        curr = self.head.next

        # iterate curr while its not null
        while curr:
            if i == index: # index found
                return curr.value 
            curr = curr.next
            i += 1
        
        return -1 # index out of bounds

    def insertHead(self, val: int) -> None:
        new_node = Node(val) # create new Node
        # Note: Dummy node is not the real head
        new_node.next = self.head.next 
        self.head.next = new_node # dummy points to new node
        if not new_node.next: # if the list was empty
            self.tail = new_node # don't forget the tail

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        # link up the new tail
        self.tail.next = new_node 
        self.tail = new_node

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head # curr is actually BEFORE_curr

        while curr and i < index: # iterate to the index
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next # removing = unlinking
            return True
        
        return False # out of bounds

    def getValues(self) -> List[int]:
        values = [] # values to be returned 
        curr = self.head.next
        while curr:
            values.append(curr.value) # get val at curr
            curr = curr.next
        return values
