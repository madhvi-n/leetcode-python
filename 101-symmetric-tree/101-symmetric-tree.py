# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_symmetric(subtree_1, subtree_2):
            if not subtree_1 and not subtree_2:
                return True
            
            if not subtree_1 or not subtree_2:
                return False

            return (subtree_1.val == subtree_2.val
                    and check_symmetric(subtree_1.left, subtree_2.right)
                    and check_symmetric(subtree_1.right, subtree_2.left)
                )
        return not root or check_symmetric(root.left, root.right)