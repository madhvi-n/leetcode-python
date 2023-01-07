# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node1, node2, height):
            if node1 is None or node2 is None:
                return
            
            if height % 2 == 1:
                node1.val, node2.val = node2.val, node1.val
            
            dfs(node1.left, node2.right, height + 1)
            dfs(node1.right, node2.left, height + 1)
            
        dfs(root.left, root.right, 1)
        return root
                