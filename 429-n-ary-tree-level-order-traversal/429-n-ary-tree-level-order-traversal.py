"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:        
        queue = [root]
        res = []
        
        while queue:
            nodes = []
            level = []
            for node in queue:
                if node:
                    nodes.append(node.val)
                    if node.children:
                        level.extend(node.children)
            if nodes:
                res.append(nodes)
            queue = level
        return res
            