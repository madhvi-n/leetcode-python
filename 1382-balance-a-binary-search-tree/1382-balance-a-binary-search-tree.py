# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.nodes = []
        
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
            
        def createBST(array):
            if not array:
                return None
            mid = len(array) // 2
            root = TreeNode(array[mid])
            root.left = createBST(array[:mid])
            root.right = createBST(array[mid + 1:])
            return root
        
        self.nodes = inorder(root)
        return createBST(self.nodes)    