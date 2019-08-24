class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
            
        rDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        for n in range(len(s)):
            num += rDict.get(s[n])
            if s[n] == 'I'and n<len(s)-1 and (s[n+1] == 'V' or s[n+1]=='X'):
                num -= 2
            if s[n] == 'X'and n<len(s)-1 and (s[n+1] == 'L' or s[n+1]=='C'):
                num -= 20
            if s[n] == 'C'and n<len(s)-1 and (s[n+1] == 'D' or s[n+1]=='M'):   
                num -= 200
        return num