class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # minimum for max_profit = 0
        # 1 entry, 1 exit allowed
        # keek track buy, sell and may profit
        # buy cannot come after sell

        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else:
                buy = sell

            sell += 1

        return max_profit
