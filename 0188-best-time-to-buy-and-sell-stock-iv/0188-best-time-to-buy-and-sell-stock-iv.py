class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
#         @lru_cache(None)
#         def recurse(i, stock, count):
#             if i >= n: return 0
#             if count >= k: return 0
            
#             buy = (-prices[i] + recurse(i+1, 1, count)) if stock == 0 else -inf
#             sell = (prices[i] + recurse(i+1, 0, count+1)) if stock == 1 else -inf
#             hold = recurse(i+1, stock, count)
            
#             return max(buy, sell, hold)
            
#         n = len(prices)
#         return recurse(0, 0, 0)

        n = len(prices)
        if k >= n // 2:
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

        dp = [[0] * n for _ in range(k + 1)]

        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])

        return dp[k][n - 1]
