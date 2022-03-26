# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(root, curr_path):
            if root is None:
                return
            
            if root.left is None and root.right is None:
                res.append(curr_path + str(root.val))
            
            if root.left:
                dfs(root.left, curr_path + str(root.val) + "->")
            
            if root.right:
                dfs(root.right, curr_path + str(root.val) + "->")
            
        dfs(root, "")
        return res