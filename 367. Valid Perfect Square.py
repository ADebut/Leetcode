class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        mid = (low+high) // 2
        while(low <= high):
            if mid * mid > num:
                high = mid - 1
            elif mid * mid < num:
                low = mid + 1
            else:
                return True
            mid = (low + high) // 2
        return False