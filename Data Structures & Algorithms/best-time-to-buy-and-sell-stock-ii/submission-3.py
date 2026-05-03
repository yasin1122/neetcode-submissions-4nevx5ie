class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # need 2 pointer while iterating
        # if no profit possible iterate, if possible buy
        # hold if you can make more, sell if you cant
        # if you buy set the sell pointer at buy and iterate that

        if len(prices) < 2:
            return 0

        profit = 0

        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]

        return profit

