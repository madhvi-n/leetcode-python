class Solution:
    def countOnes(self, n: int) -> int:
        ans = 0
        
        while n != 0:
            n = n & (n-1)
            ans += 1
        return ans
    
    def countBits(self, n: int) -> List[int]:
        res = []
        
        for i in range(0, n + 1):
            ones = self.countOnes(i)
            res.append(ones)
        return res
            