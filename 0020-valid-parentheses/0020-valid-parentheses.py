class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        
        for char in s:
            if stack and stack[-1] == hashmap.get(char):
                stack.pop()
            else:
                stack.append(char)
        return not stack