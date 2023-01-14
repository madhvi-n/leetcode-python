# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
#         def count(node: TreeNode, parentVal: int) -> int:
#             if node is None:
#                 return 0
#             currentMax = max(node.val, parentVal)
#             return (node.val >= parentVal) + count(node.left, currentMax) + count(node.right, currentMax)
        
#         return count(root, root.val)

        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)
