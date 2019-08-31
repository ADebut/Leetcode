class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: [] for i in range(9)}
        cols = {j: [] for j in range(9)}
        blocks = {b: [] for b in range(9)}
        
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == '.':
                    continue
                block_num = (i//3 * 3) + j//3
                if col in rows[i] or col in cols[j] or col in blocks[block_num]:
                    return False
                
                rows[i].append(col)
                cols[j].append(col)
                blocks[block_num].append(col)
        return True