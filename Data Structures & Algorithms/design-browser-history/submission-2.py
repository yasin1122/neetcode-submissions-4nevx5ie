class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.curr.next = new_node
        new_node.prev = self.curr
        self.curr = new_node

    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.curr.prev:
            i += 1
            self.curr = self.curr.prev
            if i == steps:
                return self.curr.val
        return self.curr.val

    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.curr.next:
            i += 1
            self.curr = self.curr.next
            if i == steps:
                return self.curr.val
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)