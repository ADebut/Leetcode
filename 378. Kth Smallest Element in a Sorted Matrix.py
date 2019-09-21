import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        queue = []
        for i in range(len(matrix)):
            queue.append((matrix[i][0], i, 0))
        heapq.heapify(queue)
        
        for i in range(k - 1):
            row, col = queue[0][1], queue[0][2]
            if col < len(matrix[0]) - 1:
                heapq.heappop(queue)
                heapq.heappush(queue, (matrix[row][col + 1], row, col + 1))
            else:
                heapq.heappop(queue)
        return queue[0][0]