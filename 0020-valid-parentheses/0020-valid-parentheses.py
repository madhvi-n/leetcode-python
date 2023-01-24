class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if stack and hashmap.get(char) == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0