class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        c = collections.Counter(barcodes)
        pq = []
        # c = sorted(dic.items(), key = lambda k: k[1], reverse = True)
        for key, value in c.items():
            heapq.heappush(pq, (-value, key))
        p_a, p_b = 0, ''
        res = []
        while pq:
            a, b = heapq.heappop(pq)
            res.append(b)
            if p_a < 0:
                heapq.heappush(pq, (p_a, p_b))
            a += 1
            p_a, p_b = a, b

        if len(res) != len(barcodes): return []
        return res