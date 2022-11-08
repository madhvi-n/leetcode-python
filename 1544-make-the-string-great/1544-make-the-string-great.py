class Solution:
    def makeGood(self, s: str) -> str:
        
#         while len(s) > 1:
#             find = False
            
#             for i in range(len(s) - 1):
#                 curr_char, next_char = s[i], s[i+1]
#                 if abs(ord(curr_char) - ord(next_char)) == 32:
#                     s = s[:i] + s[i+2:]
                    
#                     find = True
#                     break
#             if not find:
#                 break
        
#         return s

        stack = []
        
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)