class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1:
            return list(matrix[0])
        elif len(matrix) > 1:
            A = zip(*matrix[1:])
            return list(matrix[0]) + self.spiralOrder(list(A)[::-1])
        