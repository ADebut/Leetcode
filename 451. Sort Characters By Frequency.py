class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic=collections.defaultdict(int)
        for k in s:
            dic[k]+=1
        heap=[(-val,key) for key,val in dic.items()]
        heapq.heapify(heap)
        res=''
        while heap:
            val,key=heapq.heappop(heap)
            res+=key*(-val)
        return res