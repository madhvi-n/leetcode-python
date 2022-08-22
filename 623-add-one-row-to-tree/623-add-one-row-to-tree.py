# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        return self.dfs(root, val, depth, 1, 0)
    
    def dfs(self, node, val, depth, height, direction):
        if node is None:
            if height == depth:
                return TreeNode(val)
            else:
                return None
            
        if height == depth:
            temp = TreeNode(val)
            if direction == 0:
                temp.left = node
            elif direction == 1:
                temp.right = node
            return temp
        node.left = self.dfs(node.left, val, depth, height + 1, 0)
        node.right = self.dfs(node.right, val, depth, height + 1, 1)
        return node