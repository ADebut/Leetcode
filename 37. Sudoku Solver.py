class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solver(board)
        
    def solver(self, board):
        for i in range(9):
            for j in range(9):
                if (board[i][j] == '.'):
                    count = '1'
                    while (count <= '9'):
                        if (self.isValid(i, j, board, count)):
                            board[i][j] = count
                            if (self.solver(board)):
                                return True
                            else:
                                #下一个位置没有数字，就还原，然后当前位置尝试新的数
                                board[i][j] = '.'
                        count = chr(ord(count) + 1)
                    return False
        return True
    
    def isValid(self, row, col, board, c):
        for i in range(9):
            if (board[row][i] == c):
                return False

        for i in range(9):
            if (board[i][col] == c):
                return False

        start_row = row // 3 * 3;
        start_col = col // 3 * 3;
        for i in range(3):
            for j in range(3):
                if (board[start_row + i][start_col + j] == c):
                    return False
        return True