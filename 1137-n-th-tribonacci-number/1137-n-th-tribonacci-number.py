class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1 or n == 2:
            return 1
        
        n1, n2, n3 = 0, 1, 1
        
        for i in range(3, n+1):
            res = n1 + n2 + n3
            n1, n2, n3 = n2, n3, res
        return res