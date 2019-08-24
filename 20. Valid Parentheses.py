class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in mapping:
                if stack: 
                    top = stack.pop()
                else:
                    top = 't'
                if mapping[c] != top:
                    return False
            else:
                stack.append(c)
        return not stack