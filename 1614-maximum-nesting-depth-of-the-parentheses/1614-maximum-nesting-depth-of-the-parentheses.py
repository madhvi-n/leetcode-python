class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        currDepth = 0
        
        # traverse through string
        # for each open paranthesis, increment currentDepth and calculate maxDepth
        # for each closed paranthesis, decrement currentDepth
        
        for char in s:
            if char == '(':
                currDepth += 1
                maxDepth = max(maxDepth, currDepth)
            if char == ')':
                currDepth -= 1
        return maxDepth
        