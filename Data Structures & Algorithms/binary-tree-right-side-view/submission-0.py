# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we can store each level in an arr and return only the list of last items

        q = deque()
        if root:
            q.append(root)
        result = []

        while q:
            visible_val = None
            for i in range(len(q)):
                node = q.popleft()
                visible_val = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(visible_val)


        return result