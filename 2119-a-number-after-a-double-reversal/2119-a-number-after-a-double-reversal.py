class Solution:
    def reverse(self, x: int) -> int:
        n = 0
        rem = 0
        
        while x > 0:
            rem = x % 10
            x = x // 10
            n = (n * 10) + rem
        return n
    
    def isSameAfterReversals(self, num: int) -> bool:
        ans = 0
        ans = self.reverse(num)
        return num == self.reverse(ans)
            
            