# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.answer = None
        
        def dfs(originalNode, clonedNode):
            if originalNode:
                dfs(originalNode.left, clonedNode.left)
                
                if originalNode == target:
                    self.answer = clonedNode
                
                dfs(originalNode.right, clonedNode.right)
        
        dfs(original, cloned)
        return self.answer