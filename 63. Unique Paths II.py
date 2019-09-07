class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        
        dp = [0 for i in range(n)]
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                dp[i] = 0
                break
            else:
                dp[i] = 1
        for i in range(i + 1, n):
            dp[i] = 0
        for i in range(1, m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    if j != 0:
                        dp[j] = dp[j] + dp[j - 1]
        return dp[n-1]