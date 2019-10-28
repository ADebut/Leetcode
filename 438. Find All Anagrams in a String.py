class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        # pdict = collections.Counter(p)
        # i = 0
        # j = len(p) - 1
        # ans = []
        # while j < len(s):
        #     sdict = collections.Counter(s[i: j + 1])
        #     for k in pdict:
        #         sdict[k] -= pdict[k]
        #     s_set = set(list(sdict.values()))
        #     if len(s_set) == 1 and 0 in s_set:
        #         ans.append(i)
        #     i += 1
        #     j += 1
        # return ans
        dic1 = [0]*26
        dic2 = [0]*26
        res = []
        for i in range(len(p)):
            dic1[ord(p[i])-ord('a')] += 1
            dic2[ord(s[i])-ord('a')] += 1
        if dic1 == dic2:
            res.append(0)
        for i in range(1, len(s)-len(p)+1):
            dic2[ord(s[i-1])-ord('a')] -= 1
            dic2[ord(s[i+len(p)-1])-ord('a')] += 1
            if dic1 == dic2:
                res.append(i)
        return res
        