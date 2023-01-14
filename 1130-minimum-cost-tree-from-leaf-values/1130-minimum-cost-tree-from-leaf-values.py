class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [float('inf')]
        
        for node in arr:
            while stack[-1] <= node:
                mid = stack.pop()
                res += mid * min(stack[-1], node)
            stack.append(node)
            
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res