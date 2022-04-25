class Solution:
    def checkGoodTriplets(self, first: int, second: int, third: int, a: int, b: int, c:int ) -> bool:
        return abs(first - second) <= a and abs(second - third) <= b and abs(first - third) <= c
        
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        length = len(arr)
        count = 0
        
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    if self.checkGoodTriplets(arr[i], arr[j], arr[k], a, b, c):
                        count += 1
        return count