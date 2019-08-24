class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        l = min([len(x) for x in strs])
        cnt = 0
        for i in range(l):
            pre = strs[0][i]
            for s in strs:
                if s[i] == pre:
                    continue
                else:
                    return s[:cnt]
            cnt += 1
        return strs[0][:cnt]