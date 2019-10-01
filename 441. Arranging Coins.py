class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while end >= start:
            mid = (start+end)//2
            total = mid*(mid+1)//2
            if total == n:
                return mid
            elif total < n:
                start = mid + 1
            else:
                end = mid - 1
        return end