class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for operator in operations:  
            if operator == "C" and stack:
                stack.pop()
            
            elif operator == "D":
                stack.append(stack[-1] * 2)
            
            elif operator == "+":
                stack.append(stack[-1] + stack[-2])
            
            else:
                stack.append(int(operator))
        
        return sum(stack) if stack else 0