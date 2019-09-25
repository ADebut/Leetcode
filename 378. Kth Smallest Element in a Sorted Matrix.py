class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        heap = [(matrix[0][0],0,0)]
        visited = set((0,0))
        res = None
        while k > 0:
            res = heapq.heappop(heap)
            r, c = res[1], res[2]
            if r+1 < m and (r+1,c) not in visited:
                heapq.heappush(heap, (matrix[r+1][c], r+1, c))
                visited.add((r+1,c))
            if c+1 < n and (r,c+1) not in visited:
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))
                visited.add((r,c+1))
            k -= 1
        return res[0]
            