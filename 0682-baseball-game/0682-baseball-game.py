class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for operation in operations:
            # if operation not in ["C", "D", "+"]:
            #     stack.append(int(operation))
                
            if operation == "C" and stack:
                stack.pop()
            
            elif operation == "D":
                stack.append(stack[-1] * 2)
            
            elif operation == "+":
                stack.append(stack[-1] + stack[-2])
            
            else:
                stack.append(int(operation))
        
        return sum(stack) if stack else 0