# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node, parent, depth, child):
            if node:
                if node.val == child:
                    return depth, parent
                return dfs(node.left, node, depth + 1, child) or dfs(node.right, node, depth + 1, child)
            
        xDepth, xParent = dfs(root, None, 0, x)
        yDepth, yParent = dfs(root, None, 0, y)
        return xDepth == yDepth and xParent != yParent