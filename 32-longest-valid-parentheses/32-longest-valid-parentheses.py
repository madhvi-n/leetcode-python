class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        stack = [-1]
        max_value = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_value = max(max_value, i - stack[-1])
        return max_value