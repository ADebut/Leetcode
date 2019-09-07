class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        sell = 0
        buy = 0
        while(sell < len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                maxprofit = max(maxprofit, prices[sell] - prices[buy])
            sell += 1
        return maxprofit