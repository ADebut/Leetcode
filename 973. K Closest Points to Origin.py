class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        for i in range(len(points)):
            points[i].append(points[i][0]**2 + points[i][1]**2)
        points.sort(key = lambda k: k[2])
        for i in range(K):
            points[i] = points[i][:2]
        return points[:K]