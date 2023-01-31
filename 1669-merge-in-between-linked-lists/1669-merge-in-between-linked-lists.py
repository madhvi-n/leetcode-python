# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        left = list1
        
        # Move left till a - 1, prev to target
        for _ in range(a - 1):
            left = left.next 

        right = left
        for i in range(b - a + 1):
            right = right.next

        # Connect left's next to list2 and traverse list2
        left.next = list2
        while list2.next:
            list2 = list2.next
        
        # Connect list2's next to right's next
        list2.next = right.next
		
        return list1