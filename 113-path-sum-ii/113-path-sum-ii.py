# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, target, lst, result):
        if root.left is None and root.right is None:
            if root.val == target:
                result += [lst + [root.val]]
                
        if root.left:
            self.helper(root.left, target - root.val, lst + [root.val], result)
        
        if root.right:
            self.helper(root.right, target - root.val, lst + [root.val], result)
        
        return result
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        return self.helper(root, targetSum, [], [])