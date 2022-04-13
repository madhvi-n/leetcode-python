class Solution:
    def string(self, s):
        stack = []

        for char in s:
            if char == "#" and stack:
                stack.pop()
            elif char != "#":
                stack.append(char)

        return "".join(stack)
        
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = self.string(s)
        t = self.string(t)
        
        return s == t
        
        