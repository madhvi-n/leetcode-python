class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        sqrRoot = 0
        
        while start <= end:
            mid = int(start + (end - start) // 2)
            
            sqr = mid * mid
            
            if sqr == x:
                return mid
            
            if sqr < x:
                sqrRoot = mid
                start = mid + 1
            else:
                end = mid - 1
        
        return sqrRoot
            