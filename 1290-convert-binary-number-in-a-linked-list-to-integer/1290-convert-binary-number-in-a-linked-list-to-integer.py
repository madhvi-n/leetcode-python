# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        num = head.val
        
        while curr.next:
            num = num * 2 + curr.next.val
            curr = curr.next
        return num