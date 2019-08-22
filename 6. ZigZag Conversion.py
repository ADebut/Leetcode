class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        middle = ['' for x in range(numRows)]
        row = 0
        down = True
        if numRows == 1:
            return s
        for each in s:
            middle[row] += each
            if down:
                if row == numRows-1:
                    down = False
                    row -= 1
                else:
                    row += 1
            else:
                if row == 0:
                    down = True
                    row += 1
                else:
                    row -= 1
        return ''.join(middle)