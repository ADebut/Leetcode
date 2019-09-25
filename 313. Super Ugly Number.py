class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        heap = [1]
        visited = set([1])
        
        for i in range(n):
            val = heapq.heappop(heap)
            
            for factor in primes:
                if val*factor not in visited:
                    heapq.heappush(heap, val*factor)
                    visited.add(val*factor)
        
        
        return val