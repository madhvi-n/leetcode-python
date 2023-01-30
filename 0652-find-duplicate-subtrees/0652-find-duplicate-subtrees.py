# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count = defaultdict(int)
        res = []
        
        def traverse(node):
            if not node:
                return ""
            
            rep = ("(" + traverse(node.left) + ")" + str(node.val) + 
                   
                   "(" + traverse(node.right) + ")"
                  
                  )
            count[rep] += 1
            if count[rep] == 2:
                res.append(node)
            return rep
        
        traverse(root)
        return res
        
        