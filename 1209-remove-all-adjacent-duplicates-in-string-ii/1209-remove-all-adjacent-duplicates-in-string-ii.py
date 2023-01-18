class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Use dummy element ('#', 0) to avoid empty stack.
        
        stack = [['#', 0]]
        
        # traverse through string
        # store chars in stack as (char, charCount)
        # for each char, if top char is equal to current char, increment top char's count, 
        # else append char with it's count
        # when the top char's count reaches k, pop the char from stack
        # return string in the form char * charCount using join
        
        for char in s:
            if stack[-1][0] == char:
                stack[-1][1] += 1
                
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        return ''.join(c * k for c, k in stack)