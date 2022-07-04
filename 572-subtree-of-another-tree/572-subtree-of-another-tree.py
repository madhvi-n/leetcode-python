# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sameTree(self, node1, node2):
            if not node1 and not node2:
                return True
            if node1 and node2 and node1.val == node2.val:
                return self.sameTree(node1.left, node2.left) and self.sameTree(node1.right, node2.right)
            return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if not subRoot:
            return True
        
        # subroot of a root can be sametree hence checking if both are same tree
        # if not, recursively checkif subRoot lies in left of root or right
        if root.val == subRoot.val and self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        