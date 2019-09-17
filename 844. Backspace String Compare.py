class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = []
        for i in range(len(S)):
            if S[i] == '#' and s:
                s.pop()
            elif S[i] != '#':
                s.append(S[i])
        t = []
        for i in range(len(T)):
            if T[i] == '#' and t:
                t.pop()
            elif T[i] != '#':
                t.append(T[i])
        if t == s:
            return True
        else:
            return False