# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head: Optional[ListNode], ):
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        mid = self.middleNode(head)
        
        rl = self.reverseList(mid)
        
        maxSum = 0
        while rl:
            maxSum = max(maxSum, rl.val + head.val)
            rl = rl.next
            head = head.next
            
        return maxSum
        