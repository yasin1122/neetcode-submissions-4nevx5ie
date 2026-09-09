class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        node = Node(key, val)
        if self.root == None:
            self.root = node
        curr = self.root
        while curr:
            if key < curr.key:
                if curr.left == None:
                    curr.left = node
                curr = curr.left
            elif key > curr.key:
                if curr.right == None:
                    curr.right = node
                curr = curr.right
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1
    
    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def getMin(self) -> int:
        curr = self.findMin(self.root)
        return curr.val if curr else -1

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1
    
    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr == None:
            return None

        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left == None:
                return curr.right
            elif curr.right == None:
                return curr.left
            else:
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root != None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result
