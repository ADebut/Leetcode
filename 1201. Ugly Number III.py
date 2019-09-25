class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(a, b):
            return (a * b) // math.gcd(a, b) # a, b, c >= 1
        
        def count(val, a, b, c):
            return (val // a) + (val // b) + (val // c) - (val // lcm(a, b)) - \
                   (val // lcm(a, c)) - (val // lcm(b, c)) + (val // lcm(lcm(a, b), c))
        
        low = 1
        high = 2*10**9
        
        while low < high:
            mid = low + (high - low) // 2
            if count(mid, a, b, c) < n:
                low = mid + 1
            else:
                high = mid
        return low