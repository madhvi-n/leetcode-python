class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = remaining = 0
        while numBottles:
            ans += numBottles
            numBottles, remaining = divmod(numBottles + remaining, numExchange)
        return ans