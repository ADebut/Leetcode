class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            if n <= 1:
                return True
            else:
                return False
        if len(edges) != n- 1:
            return False
        dic = collections.defaultdict(list)
        for i in range(len(edges)):
            dic[edges[i][0]].append(edges[i][1])
            dic[edges[i][1]].append(edges[i][0])
        
        visited = []
        stack = [edges[0][0]]
        while(stack):
            i = stack.pop(0)
            if i not in visited:
                visited.append(i)
                for k in dic[i]:
                    stack.append(k)
        return len(visited) == n
                