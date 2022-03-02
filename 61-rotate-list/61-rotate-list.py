# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        #Find length and last node of list
        length = 1
        tail = head
        while tail.next is not None:
            tail = tail.next
            length += 1
        
        #Reduce rotations by using k mod length
        k = k % length
        
        #In case k is 0, return head
        if k == 0:
            return head
        
        #Find the node prev to Kth node from end
        curr = head
        for _ in range(length - k - 1):
            curr = curr.next
        
        #New head with the node next to prev, here next to the current
        #Store new head, assign curr.next to None and link last node's next to head
        newHead = curr.next
        curr.next = None
        tail.next = head
        
        return newHead