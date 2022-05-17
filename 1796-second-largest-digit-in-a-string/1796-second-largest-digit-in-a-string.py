class Solution:
    def secondHighest(self, s: str) -> int:
        stack = []
        
        for char in s:
            if char not in stack and char.isdigit():
                stack.append(char)
        stack.sort(reverse=True)
        return stack[1] if len(stack) >= 2 else -1
