# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.nodes = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.nodes.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        return min(b - a for a, b in zip(self.nodes, self.nodes[1:]))