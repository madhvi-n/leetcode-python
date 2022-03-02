# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head: Optional[ListNode]) -> int:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        return length
    
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            head = None
            return head
        
        middleNode = self.length(head) // 2
        
        node = head
        count = 0
    
        while node:
            if count == middleNode - 1:
                #node.next is the node to be removed
                # so simply assign node.next.next to node.next
                node.next = node.next.next
                break
                
            node = node.next
            count += 1
        return head
        