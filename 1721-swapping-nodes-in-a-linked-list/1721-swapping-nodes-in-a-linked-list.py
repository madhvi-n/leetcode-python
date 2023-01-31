# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        dummy = ListNode(0, head)
        
        left = right = head
        
        for i in range(k - 1):
            left = left.next
        
        for i in range(length - k):
            right = right.next
        
        left.val, right.val = right.val, left.val
        return dummy.next