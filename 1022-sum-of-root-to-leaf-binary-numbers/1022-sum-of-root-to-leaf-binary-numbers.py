# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
#         root_to_leaf = 0
#         stack = [(root, 0) ]
        
#         while stack:
#             root, curr_number = stack.pop()
#             if root is not None:
#                 curr_number = (curr_number << 1) | root.val
#                 # if it's a leaf, update root-to-leaf sum
                
#                 if root.left is None and root.right is None:
#                     root_to_leaf += curr_number
#                 else:
#                     stack.append((root.right, curr_number))
#                     stack.append((root.left, curr_number))
#         return root_to_leaf

        self.root_to_leaf = 0
        def preorder(node, curr):
            if node:
                curr = curr << 1 | node.val
                
                if not node.left and not node.right:
                    self.root_to_leaf += curr
                
                preorder(node.left, curr)
                preorder(node.right, curr)
        
        preorder(root, 0)
        return self.root_to_leaf
