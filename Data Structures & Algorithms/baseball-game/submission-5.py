class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def push(self, val):
        new_node = Node(int(val))
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node

        self.tail.prev = new_node

    def pop(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def get_last_val(self):
        return self.tail.prev.val

    def get_second_last_val(self):
        return self.tail.prev.prev.val

    def get_total(self):
        total = 0
        curr = self.head.next
        while curr != self.tail:
            total += curr.val

            curr = curr.next
        return total

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        op_stack = Stack()

        for op in operations:
            match op:
                case '+':
                    op_stack.push(op_stack.get_last_val() + op_stack.get_second_last_val())
                case 'D':
                    op_stack.push(op_stack.get_last_val() * 2)
                case 'C':
                    op_stack.pop()
                case _:
                    op_stack.push(op)

        return op_stack.get_total()





