# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root: Optional[TreeNode]) -> bool:
        elements = []
        
        if root is None:
            return None
        
        if root.left:
            elements += self.inorder(root.left)
        
        elements.append(root.val)
        
        if root.right:
            elements += self.inorder(root.right)
        
        return elements
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        elements = self.inorder(root) 
        
        hashMap = {}
        
        for num in elements:
            diff = k - num
            
            if diff in hashMap:
                return True
            else:
                hashMap[num] = index
        return False
        
        