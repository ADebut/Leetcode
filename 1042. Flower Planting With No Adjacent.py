class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        res = [0] * N
        #building graph from list of edges 
        G = [[] for i in range(N)]
        for x, y in paths:                   
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)   
        for i in range(N):
            used_colors = []
            for neighbor in G[i]:
                used_colors.append(res[neighbor])
            for color in range(1, 5):
                if color not in used_colors:
                    res[i] = color
        return res