class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        l = len(x)
        if x[0] in ['+', '-']:
            return False
        if l % 2 == 0:
            for i in range(int(l/2)):
                if x[i] == x[l - i - 1]:
                    continue
                else:
                    return False

                
        elif l % 2 == 1:
            for i in range(int(l/2)):
                if x[i] == x[l - i - 1]:
                    continue
                else:
                    return False
        return True