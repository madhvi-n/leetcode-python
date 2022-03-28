# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leaf_sum(self, root, left: bool):
        if root is None:
            return 0

        if root.left is None and root.right is None and left:
            return root.val

        return self.leaf_sum(root.left, True) + self.leaf_sum(root.right, False)
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.leaf_sum(root, False)