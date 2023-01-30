class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def recurse(i, stock):
            if i >= n: return 0
            
            buy = (-prices[i] + recurse(i+1, 1)) if stock == 0 else -inf
            sell = (prices[i] + recurse(i+1, 0)) if stock == 1 else -inf
            hold = recurse(i+1, stock)
            
            return max(buy, sell, hold)
            
        n = len(prices)
        return recurse(0, 0)