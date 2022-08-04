# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev, curr = list1, list1
        i = 0
        
        while i != a:
            prev = curr
            curr = curr.next
            i += 1
        
        while i != b:
            curr = curr.next
            i += 1
        prev.next = list2
        
        while list2.next is not None:
            list2 = list2.next
            
        list2.next = curr.next
        
        return list1