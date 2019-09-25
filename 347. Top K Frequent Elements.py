class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        result = []
        myDict = collections.Counter(nums)
        for key in myDict:
            temp = (myDict[key], key)
            if len(heap) >= k:
                heapq.heappushpop(heap, temp)
            else:
                heapq.heappush(heap, temp)
        for i in range(len(heap)):
            result.append(heapq.heappop(heap)[1])
        return result[::-1]
            