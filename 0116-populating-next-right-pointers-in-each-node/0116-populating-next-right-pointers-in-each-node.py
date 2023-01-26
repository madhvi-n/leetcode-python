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
        result = []
        
        while queue:
            next_level = []
            current_level = []
            for node in queue:
                current_level.append(node)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
            result.append(current_level)
        
        for levels in result:
            if len(levels) == 1:
                node = levels[0]
                node.next = None
            else:
                for i in range(len(levels) - 1):
                    curr = levels[i]
                    curr.next = levels[i+1]
        return root