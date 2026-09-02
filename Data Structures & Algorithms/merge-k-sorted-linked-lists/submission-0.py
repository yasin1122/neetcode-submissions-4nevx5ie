# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        flat_list = []
        
        for node in lists:
            while node:
                flat_list.append(node.val)
                node = node.next
        
        flat_list.sort()
        for val in flat_list:
            curr.next = ListNode(val)
            curr = curr.next

        return head.next

            