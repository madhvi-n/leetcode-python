class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x, y = min(nums), max(nums)
        
        if x == y:
            return x
        
        while y:
            x, y = y, x % y
        return x
        