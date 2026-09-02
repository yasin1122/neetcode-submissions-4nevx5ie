# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        sentinel = ListNode()
        tail = sentinel

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next)) 

        return sentinel.next      
        
        # my original solution, less efficient O(n log n) vs above is N log K
        # push all values to min heap
        # pop them and attach them to a new linked list, return head

        min_heap = []
        sentinel = ListNode()
        tail = sentinel

        for node in lists:
            while node:
                heapq.heappush(min_heap, node.val)
                node = node.next

        while min_heap:
            tail.next = ListNode(heapq.heappop(min_heap))
            tail = tail.next

        return sentinel.next