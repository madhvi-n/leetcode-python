# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            elements = set()
            
            if root is None:
                return None

            elements.add(root.val)

            if root.left:
                left = helper(root.left)
                elements.update(left)

            if root.right:
                right = helper(root.right)
                elements.update(right)
            return elements
        
        return len(helper(root)) == 1
    