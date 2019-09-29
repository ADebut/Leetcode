class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        dist = {node: float('inf') for node in xrange(1, N+1)}
        
        def dfs(start, time):
            if time >= dist[start]: return
            dist[start] = time
            for timeslot, target in sorted(graph[start]):
                dfs(target, time + timeslot)
        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1