class Solution:
    def checkValidString(self, s: str) -> bool:
        open_brackets = close_brackets = 0
        
        n = len(s)
        
        for i in range(n):
            # if char is ( or * - we increment open_brackets value
            if s[i] in "(*":
                open_brackets += 1
            # else decrement it
            else:
                open_brackets -= 1
            
            # we check right balance value starting from the end (right side)
            if s[n-i-1] in "*)":
                close_brackets += 1
            else:
                close_brackets -= 1
            
            # if any balance goes negative we have the case where order of parenthesis is wrong
            # e.g. )(  -> open_brackets will be -1 and rightBalance will be -1 after first iteration
            # or ((( - open_brackets is OK, but rightBalance will be -1 after first iteration
            
            if open_brackets < 0  or close_brackets < 0:
                return False
        return True
        