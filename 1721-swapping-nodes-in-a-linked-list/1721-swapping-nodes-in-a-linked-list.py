# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        # Find the length of the linked list
        current = head
        length = 0
        while current:
            length += 1
            current = current.next

        # Check if k is within bounds
        if k > length:
            return head

        current = head
        prev = None
        for i in range(1,  k):
            prev = current
            current = current.next

        # Find kth node from end
        kth_node_from_end = head
        for i in range(length - k):
            kth_node_from_end = kth_node_from_end.next

        # Swap data of nodes
        current.val, kth_node_from_end.val = kth_node_from_end.val, current.val

        return head