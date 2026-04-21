# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = deque()
        curr = head
        while curr:
            stack.append(curr)
            if curr.next:
                curr = curr.next
            else:
                break
        while stack:
            temp = stack.pop()
            if stack:
                temp.next = stack[-1]
            else:
                temp.next = None
        return curr