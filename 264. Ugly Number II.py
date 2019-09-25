import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = [1]
        visited = set([1])
        
        for i in range(n):
            val = heapq.heappop(heap)
            
            for factor in [2,3,5]:
                if val*factor not in visited:
                    heapq.heappush(heap, val*factor)
                    visited.add(val*factor)
        
        
        return val