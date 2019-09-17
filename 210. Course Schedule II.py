class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        G = [[] for i in range(numCourses)]
        degree = [0] * numCourses
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        queue = [i for i in range(numCourses) if degree[i] == 0]
        path = []
        while(True):
            if not queue:
                flag = True
                for i in range(numCourses):
                    if degree[i]:
                        flag = False
                if flag:
                    return path
                else:
                    return []
            now = queue.pop(0)
            path.append(now)
            for i in G[now]:
                degree[i] -= 1
                if degree[i] == 0:
                    queue.append(i)
                    