class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         first_buy, first_sell = [0] * n, [0] * n
#         second_buy, second_sell = [0] * n, [0] * n

#         first_buy[0] = -prices[0]
#         first_sell[0] = 0
#         second_buy[0] = -prices[0]
#         second_sell[0] = 0

#         for i in range(1, n):
#             first_buy[i] = max(first_buy[i - 1], -prices[i])
#             first_sell[i] = max(first_sell[i - 1], first_buy[i - 1] + prices[i])
#             second_buy[i] = max(second_buy[i - 1], first_sell[i - 1] - prices[i])
#             second_sell[i] = max(second_sell[i - 1], second_buy[i - 1] + prices[i])
#         return second_sell[-1]
        n = len(prices)
        first_buy, first_sell = -prices[0], 0
        second_buy, second_sell = -prices[0], 0

        for i in range(1, n):
            first_buy = max(first_buy, -prices[i])
            first_sell = max(first_sell, first_buy + prices[i])
            second_buy = max(second_buy, first_sell - prices[i])
            second_sell = max(second_sell, second_buy + prices[i])

        return second_sell
