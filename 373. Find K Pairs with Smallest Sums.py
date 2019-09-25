class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        
        heap = [(nums1[0] + nums2[0], 0, 0)] 
        visited = set()
        output = []
        
        while len(output) < k and heap:
            val = heapq.heappop(heap)
            output.append([nums1[val[1]], nums2[val[2]]])
            
            if val[1] < len(nums1) - 1 and (val[1]+1, val[2]) not in visited:
                visited.add((val[1]+1, val[2]))
                heapq.heappush(heap, (nums1[val[1] + 1] + nums2[val[2]], val[1] + 1, val[2]))
            if val[2] < len(nums2) - 1 and (val[1], val[2] + 1) not in visited:
                visited.add((val[1], val[2] + 1))
                heapq.heappush(heap, (nums1[val[1]] + nums2[val[2] + 1], val[1], val[2] + 1))
        
        return output