class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def recurse(i, stock, count):
            if i >= n: return 0
            if count >= k: return 0
            
            buy = (-prices[i] + recurse(i+1, 1, count)) if stock == 0 else -inf
            sell = (prices[i] + recurse(i+1, 0, count+1)) if stock == 1 else -inf
            hold = recurse(i+1, stock, count)
            
            return max(buy, sell, hold)
            
        n = len(prices)
        k = 1 # set number of transactions here
        return recurse(0, 0, 0)