class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        K = 2
        dp = [[0 for x in range(K + 1)] for y in range(len(prices))]
        for k in range(1, K + 1):
            mini = prices[0]
            for i in range(1, len(prices)):
                mini = min(mini, prices[i] - dp[i][k - 1])
                dp[i][k] = max(dp[i - 1][k], prices[i] - mini)
                
        return dp[len(prices) - 1][k]