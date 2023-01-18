class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        count = 0
        
        for char in s:
            if stack and stack[-1] == 'b' and char == 'a':
                stack.pop()
                count += 1
            else:
                stack.append(char)
        return count
        