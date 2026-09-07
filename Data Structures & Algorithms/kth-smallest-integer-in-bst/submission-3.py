# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = None
        self.count = 0

        def dfs(root):
            if not root:
                return None

            dfs(root.left)
            self.count += 1
            if self.count == k:
                self.result = root.val
                return
            dfs(root.right)

        dfs(root)

        return self.result

        state = [None, 0] # result, count

        def dfs(root):
            if not root:
                return None

            dfs(root.left)
            state[1] += 1
            if state[1] == k:
                state[0] = root.val
                return
            dfs(root.right)

        dfs(root)

        return state[0]