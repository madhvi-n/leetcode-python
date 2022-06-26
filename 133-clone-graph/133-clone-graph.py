"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # to keep track of old and their new nodes
        
        oldToNew = dict()
        
        def clone(node):
            if node is None:
                return
            
            # if node exists in dict, it means their copy is already created so return the copy
            if node in oldToNew:
                return oldToNew[node]
            
            # create a copy and add it to dict
            copy = Node(node.val)
            oldToNew[node] = copy
            
            # recursively create copy of node's neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            
            return copy
        
        return clone(node)