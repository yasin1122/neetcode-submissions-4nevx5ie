# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # None -> H -> 2 -> 3
        # prev <- curr  temp
        prev, curr = None, head

        while curr:
            # temp = curr.next
            # curr.next = prev
            # prev = curr
            # curr = temp
            curr.next, prev, curr = prev, curr, curr.next
        
        return prev

