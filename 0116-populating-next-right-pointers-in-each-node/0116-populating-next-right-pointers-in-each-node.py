"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        
        queue = [root]
        res = []
        
        while queue:
            levels = []
            nodes = []
            for node in queue:
                nodes.append(node)
                if node.left:
                    levels.append(node.left)
                if node.right:
                    levels.append(node.right)
            queue = levels
            res.append(nodes)
        
        for levels in res:
            if len(levels) == 1:
                node = levels[0]
                node.next = None
            else:
                for i in range(len(levels) - 1):
                    curr = levels[i]
                    curr.next = levels[i+1]
        return root