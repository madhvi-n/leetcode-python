class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        # for each price, compare it with the previous price. Since 0th price has no prev, start from index 1
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        return profit