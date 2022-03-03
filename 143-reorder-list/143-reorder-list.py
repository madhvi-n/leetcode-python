# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #Find mid node
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        #Second half starts at mid's next
        second = slow.next
        prev = slow.next = None
        
        #Reverse the second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        #Merge two lists
        first, second = head, prev
        
        while second:
            temp1, temp2 = first.next, second.next #Store next nodes of first and second's head
            first.next = second #Assign first's next to head of second
            second.next = temp1 # Assign second's next to temp which has first's next
            first, second = temp1, temp2 #Update first and second using temp1, temp2
        
            