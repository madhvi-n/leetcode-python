class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price, max_profit = float('inf'), 0

        for i in range(n):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)
        return max_profit