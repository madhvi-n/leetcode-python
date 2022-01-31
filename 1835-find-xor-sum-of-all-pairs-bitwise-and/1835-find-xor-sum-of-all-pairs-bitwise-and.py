import itertools

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        n1 = 0
        n2 = 0
        
        for num in arr1:
            n1 ^= num
        
        for num in arr2:
            n2 ^= num
        
        return n1 & n2
