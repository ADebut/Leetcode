class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s =''
        for i in str(x).strip('-'):
            s = i + s
        for j in range(len(s)):
            if s[j] == '0':
                c = j
            if s[j] != '0':
                break
        if '-' in str(x):
            s = '-' + s
        
        s = int(s)
        if s > 2**31 - 1 or s < - 2**31:
            return 0
        return int(s)