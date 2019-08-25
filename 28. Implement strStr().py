class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        j = 0
        i = 0
        while(i < len(haystack)):
            if haystack[i] == needle[j]:
                j += 1
                if (j == len(needle)):
                    return i - j + 1
            else:
                i = i - j
                j = 0
            i += 1
        return -1