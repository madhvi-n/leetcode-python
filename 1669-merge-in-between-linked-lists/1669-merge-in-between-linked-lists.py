# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev, curr = list1, list1
        index = 0
        
        while index < a:
            prev = curr
            curr = curr.next
            index += 1
        
        while index < b:
            curr = curr.next
            index += 1
            
        
        prev.next = list2
        
        while list2.next is not None:
            list2 = list2.next
            
        list2.next = curr.next
        
        return list1