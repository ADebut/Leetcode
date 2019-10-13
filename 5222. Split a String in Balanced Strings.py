class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        ans = 0
        for i in s:
            if not stack:
                stack.append(i)
                continue
            if i != stack[-1]:
                stack.pop()
                if not stack:
                    ans += 1
            else:
                stack.append(i)
        return ans