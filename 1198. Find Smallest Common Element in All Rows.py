import collections
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        c = collections.Counter()
        for row in mat:
            for a in row:
                c[a] += 1
                if c[a] == len(mat):
                    return a
        return -1