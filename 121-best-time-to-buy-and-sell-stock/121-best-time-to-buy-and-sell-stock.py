class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = 0, 1
        maxProfit = 0
        
        while end < len(prices):
            if prices[start] < prices[end]:
                profit = prices[end] - prices[start]
                maxProfit = max(maxProfit, profit)
            else:
                start = end
            end += 1
        
        return maxProfit
            