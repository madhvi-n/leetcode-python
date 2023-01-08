# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.paths = []
        
        def dfs(node, currentPath):
            if not node:
                return
            
            if node and not node.left and not node.right:
                self.paths.append(currentPath + str(node.val))
            
            currentPath += str(node.val)
            
            if node.left:
                dfs(node.left, currentPath +  "->")
            
            if node.right:
                dfs(node.right, currentPath + "->")
        
        dfs(root, "")
        return self.paths