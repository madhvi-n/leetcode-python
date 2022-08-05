# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:        
        string = ""
        
        node = head
        while node:
            string += str(node.val)
            node = node.next
        
        return int(string, 2)