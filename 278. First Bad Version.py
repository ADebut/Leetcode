# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n - 1
        mid = (low + high) // 2
        while(low <= high):
            if isBadVersion(mid):
                high = mid - 1
                
            else:
                low = mid + 1
            mid = (low + high) // 2
        return low