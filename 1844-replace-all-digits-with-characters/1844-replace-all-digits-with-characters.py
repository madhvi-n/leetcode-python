class Solution:
    def replaceDigits(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char.isdigit() and stack:
                prev = ord(stack[-1]) - ord('a')
                curr = string.ascii_lowercase[prev + int(char)]
                stack.append(curr)
            else:
                stack.append(char)
            
        return "".join(stack)
                