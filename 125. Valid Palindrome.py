class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.lower()
        i = 0
        j = len(s) - 1
        while(i < j):
            while not ((ord('a') <= ord(s[i]) and ord(s[i]) <= ord('z')) or (ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'))):
                i += 1
                if i == len(s):
                    return True
            while not ((ord('a') <= ord(s[j]) and ord(s[j]) <= ord('z')) or (ord(s[j]) >= ord('0') and ord(s[j]) <= ord('9'))):
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True