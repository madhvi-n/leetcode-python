class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        res = ""
        
        for char in command:
            if stack and stack[-1] == '(' and char == ')':
                stack.pop()
                stack.append('o')
            else:
                stack.append(char)
        
        return "".join(char if char.isalpha() else "" for char in stack)