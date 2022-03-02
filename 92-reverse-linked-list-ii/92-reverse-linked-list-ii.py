# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left_prev, curr = dummy, head
        
        #Reach node at position left
        for i in range(left - 1):
            left_prev, curr = curr, curr.next
        
        #curr=left and lefPrev means node before left
        #reverse list from left to right
        prev = None
        for i in range(right - left + 1):
            temp_next = curr.next
            curr.next = prev
            prev, curr = curr, temp_next
        
        
        left_prev.next.next = curr #curr is node after right
        left_prev.next = prev
        
        return dummy.next