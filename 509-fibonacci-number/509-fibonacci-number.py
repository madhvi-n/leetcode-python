import math

class Solution:
    def fib(self, n: int) -> int:
        a =  pow((1 + math.sqrt(5))/ 2, n)
        b =  pow((1 - math.sqrt(5))/ 2, n)
        num = (a - b) / math.sqrt(5)
        return int(num)