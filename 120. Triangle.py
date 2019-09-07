class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        cols = len(triangle[-1])
        dp = [[0 for x in range(cols)] for y in range(rows)]
        dp[0][0] = triangle[0][0]
        for row in range(1, rows):
            curRow = triangle[row]
            col = 0
            dp[row][col] = dp[row - 1][col] + curRow[col]
            col += 1
            while(col < len(curRow) - 1):
                dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col]) + curRow[col]
                col += 1
            dp[row][col] = dp[row - 1][col - 1] + curRow[col]
        return min(dp[-1])