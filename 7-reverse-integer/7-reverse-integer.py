class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        remainder = 0
        
        isNegative = x < 0
        
        if isNegative: 
            x = x * -1
            
        while x > 0:
            remainder = x % 10
            x = x // 10
            ans = (ans * 10) + remainder
        
        if isNegative:
            ans = ans * -1
            
        if  -2 ** 31 > ans or ans > 2 ** 31:
            return 0
        
        return ans
        