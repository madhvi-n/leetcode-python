class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == '*' and stack:
                stack.pop()
            
            if char.isalpha():
                stack.append(char)
        
        return "".join(stack)