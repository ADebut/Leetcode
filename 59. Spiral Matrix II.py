class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        y0 = 0
        y1 = n
        x0 = 0
        x1 = n
        res = [[0]*n for _ in range(n)]
        count = 1
        while y0 < y1 and x0 < x1:
            for i in range(x0, x1):
                res[y0][i] = count
                count += 1
            for j in range(y0+1, y1-1):
                res[j][x1-1] = count
                count += 1
            if y1-1 != y0:
                for i in range(x1-1, x0-1, -1):
                    res[y1-1][i] = count
                    count += 1
            if x0 != x1-1:
                for j in range(y1-2, y0, -1):
                    res[j][x0] = count
                    count += 1
            y0 += 1
            y1 -= 1
            x0 += 1
            x1 -= 1
        return res