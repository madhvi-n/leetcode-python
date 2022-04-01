class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in "+-*/":
                left, right = stack.pop(), stack.pop()
                val = 0
                if token == "+":
                    val = right + left
                elif token == "-":
                    val = right - left
                elif token == "/":
                    val = right / left
                elif token == "*":
                    val = right * left
                stack.append(int(val))
            else:
                stack.append(int(token))
        
        return stack[-1]