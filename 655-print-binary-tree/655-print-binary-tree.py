# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def get_height(node):
            if node is None:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))
        
        def mark_node(node, row, left, right):
            nonlocal output
            if not node:
                return
            
            mid = (left + right) // 2
            
            output[row][mid] = str(node.val)
            
            mark_node(node.left, row + 1 , left, mid - 1)
            mark_node(node.right, row + 1 , mid + 1, right)
            
        height = get_height(root)
        width = 2 ** height - 1
        output = [[''] * width for _ in range(height)]
        mark_node(root, 0, 0, width - 1)
        return output