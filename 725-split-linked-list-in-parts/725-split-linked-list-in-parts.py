# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        output = []
        
        node, length = head, 0
        
        while node:
            length = length + 1
            node = node.next
        
        parts, remaining = length // k, length % k
        
        prev, curr = None, head
        
        for i in range(k):
            output.append(curr)
            
            for j in range(parts):
                if curr:
                    prev = curr
                    curr = curr.next
                    
            if remaining and curr:
                prev = curr
                curr = curr.next
                remaining -= 1
            
            if prev:
                prev.next = None
        return output