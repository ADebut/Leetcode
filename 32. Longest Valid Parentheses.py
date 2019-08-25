class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        dp = [0 for x in range(len(s))]
        for i in range(1, len(s)):
            if (s[i] == ')'):
                #右括号前边是左括号
                if (s[i - 1] == '('):
                    if i >= 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 0 + 2
                #右括号前边是右括号，并且除去前边的合法序列的前边是左括号
                elif (i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '('):
                    if i - dp[i - 1] >= 2:
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                    else:
                        dp[i] = dp[i - 1] + 2
                
                maxans = max(maxans, dp[i])
            
        
        return maxans