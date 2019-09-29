class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dic = collections.Counter(arr)
        ans = []
        for i in dic:
            if dic[i] not in ans:
                ans.append(dic[i])
            else:
                return False
        return True