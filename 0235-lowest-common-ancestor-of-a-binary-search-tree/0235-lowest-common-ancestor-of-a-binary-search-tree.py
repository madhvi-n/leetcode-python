# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        
        # for each node in root
        # if p and q are greater than node, node = node.right
        # if p and q are less than node, node = node.left
        # else return node
        
        while node:
            if p.val > node.val and q.val > node.val:
                node = node.right

            elif p.val < node.val and q.val < node.val:
                node = node.left
            
            else:
                return node