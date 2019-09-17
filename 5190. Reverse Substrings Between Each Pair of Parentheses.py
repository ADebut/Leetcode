class Solution:
    def reverseParentheses(self, s: str) -> str:
        while '(' in s:
            left = -1
            for i in range(len(s)):
                if s[i] == '(':
                    left = i
                elif s[i] == ')':
                    temp = s[left + 1: i]
                    if i < len(s) - 1:
                        s = s[:left] + temp[::-1] + s[i+1:]
                    elif i == len(s) - 1:
                        s = s[:left] + temp[::-1]
                    break
        return s