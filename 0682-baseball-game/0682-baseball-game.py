class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for operation in operations:
            if operation not in ["C", "D", "+"]:
                stack.append(int(operation))
                
            elif operation == "C" and stack:
                stack.pop()
            
            elif operation == "D":
                stack.append(stack[-1] * 2)
            
            elif operation == "+":
                a, b = int(stack[-1]), int(stack[-2])
                stack.append(a + b)
        
        return sum(stack) if stack else 0