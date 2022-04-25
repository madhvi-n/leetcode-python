# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)
        
        # Find middle node
        prev, slow, fast = None, head, head
        
        # when fast is at the end, slow will be at mid 
        while fast and fast.next:    
            prev, slow, fast = slow, slow.next, fast.next.next
        
        if prev:
            # cut the parts from mid 
            prev.next = None
        
        
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        
        return root 