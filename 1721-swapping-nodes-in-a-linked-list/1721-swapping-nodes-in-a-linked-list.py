# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, head) -> int:
        count = 0
        while head:
            head = head.next
            count += 1
        return count
        
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = self.getLength(head)
        dummy = ListNode(0, head)
        left = head
        for i in range(k - 1):
            left = left.next
        
        right = head
        for i in range(length - k):
            right = right.next
        
        left.val, right.val = right.val, left.val
        
        return dummy.next
        
