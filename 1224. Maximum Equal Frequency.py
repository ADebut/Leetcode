class Solution:
    def maxEqualFreq(self, N: List[int]) -> int:
#         if len(nums) == 1:
#             return 1
#         dic = collections.defaultdict(int)
#         flag = False
#         for i in nums:
#             dic[i] += 1

#         cnt = 0
#         for i in reversed(nums):
#             val = dic.values()
#             if len(set(val)) == 1 and 1 in val:
#                 return len(nums)
#             elif len(set(val)) == 2 and ((list(val).count(max(val)) == 1 and max(val) == 2) or list(val).count(1)) == 1:

#                 return len(nums) - cnt
#             elif 0 in val and len(set(val)) == 3 and ((list(val).count(max(val)) == 1 and max(val) == 2) or list(val).count(1)) == 1:
#                 print(dic)
#                 return len(nums) - cnt
            
#             dic[i] -= 1
#             cnt += 1
            
#         return 0
    
        L, C = len(N), collections.Counter(N)
        for i in range(L-1,-1,-1):
            print(C)
            S = set(C.values())
            if len(S) == 1 and (1 in S or len(C.values()) == 1): return i + 1
            elif len(S) == 2:
                if 1 in S and list(C.values()).count(1) == 1: return i + 1
                if list(C.values()).count(max(S)) == 1 and max(S) - min(S) == 1: return i + 1
            if C[N[i]] == 1: del C[N[i]]
            else: C[N[i]] -= 1
        return 0
		