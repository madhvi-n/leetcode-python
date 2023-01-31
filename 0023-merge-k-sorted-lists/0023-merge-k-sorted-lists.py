# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O(nlogn)
#         nodes = []
#         head = point = ListNode(0)
        
#         for curr_list in lists:
#             while curr_list:
#                 nodes.append(curr_list.val)
#                 curr_list = curr_list.next
        
#         nodes.sort()
        
#         for x in nodes:
#             point.next = ListNode(x)
#             point = point.next

#         return head.next

        dummy = curr = ListNode(0)
        heap = []
        
        for ind, el in enumerate(lists):
            if el: 
                heappush(heap, (el.val, ind))
                
        while heap:
            val, ind = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            
            if lists[ind].next:
                lists[ind] = lists[ind].next
                heappush(heap, (lists[ind].val, ind))
                
        return dummy.next