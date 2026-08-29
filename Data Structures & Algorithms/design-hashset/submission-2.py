class MyHashSet:

    def __init__(self):
        self.hash_set = []

    def add(self, key: int) -> None:
        if key not in self.hash_set:
            self.hash_set.append(key)

    def remove(self, key: int) -> None:
        index = None
        for i, val in enumerate(self.hash_set):
            if key == val:
                index = i
                break
        if index is not None:
            self.hash_set.pop(index)

    def contains(self, key: int) -> bool:
        for val in self.hash_set:
            if key == val:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)