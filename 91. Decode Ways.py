class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [0 for x in range(len(s) + 1)]
        dp[len(s)] = 1
        if s[-1] != '0':
            dp[len(s) - 1] = 1
        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0':
                continue
            ans1 = dp[i + 1]
            ans2 = 0
            if int(s[i:i+2]) <= 26:
                ans2 = dp[i + 2]
            dp[i] = ans1 + ans2
            
        return dp[0]