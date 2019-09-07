class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        sell = 1
        buy = 0
        while(sell < len(prices)):
            if prices[sell] < prices[sell - 1]:
                if sell - 1 != buy:
                    profit += prices[sell - 1] - prices[buy]
            
                buy = sell
            
            elif (sell == len(prices) - 1):
                profit += prices[sell] - prices[buy]
            sell += 1
        return profit