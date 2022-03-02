# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #find middle node
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next        
        #middle node = slow
        
        
        #Reverse the list from mid to end of linked list i.e second half
        prev = None
        
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        
        #Check palindrome
        left, right = head, prev
        
        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        
        return True
            
        
            