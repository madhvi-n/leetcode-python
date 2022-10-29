# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        dummy.next = head
        
        prefix = 0
        seen = OrderedDict()
        
        while curr:
            prefix += curr.val
            node = seen.get(prefix, curr)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = curr = curr.next
        return dummy.next