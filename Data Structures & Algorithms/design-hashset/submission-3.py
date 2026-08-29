class Node:
    def __init__(self, key = 0):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        # each index starts with a dummy node
        self.hash_set = [Node(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        curr = self.hash_set[key % 10**4]
        while curr.next:
            if curr.next.key == key:
                return # can't have duplicates
            curr = curr.next
        curr.next = Node(key)

    def remove(self, key: int) -> None:
        curr = self.hash_set[key % 10**4]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.hash_set[key % 10**4]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)