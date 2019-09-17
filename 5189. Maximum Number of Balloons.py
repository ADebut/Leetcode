class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        l = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        cnt = 0
        for i in text:
            if i in l:
                l[i] += 1
        while(True):
            for i in 'balloon':
                if l[i] > 0:
                    l[i] -= 1
                elif l[i] == 0:
                    return cnt
            cnt += 1
        return cnt