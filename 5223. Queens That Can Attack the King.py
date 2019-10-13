class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens.sort(key = lambda k:abs(k[0] - king[0]) + abs(k[1] - king[1]))
        dirs = [0] * 8
        ans = []
        for q in queens:
            if 0 not in dirs:
                break
            if dirs[0] == 0 and q[0] - king[0] == 0 and q[1] - king[1] > 0:
                ans.append(q)
                dirs[0] = 1
            elif dirs[1] == 0 and q[0] - king[0] == 0 and q[1] - king[1] < 0:
                ans.append(q)
                dirs[1] = 1
            elif dirs[2] == 0 and q[0] - king[0] > 0 and q[1] - king[1] == 0:
                ans.append(q)
                dirs[2] = 1
            elif dirs[3] == 0 and q[0] - king[0] < 0 and q[1] - king[1] == 0:
                ans.append(q)
                dirs[3] = 1
            elif dirs[4] == 0 and q[0] - king[0] > 0 and q[0] - king[0] == q[1] - king[1]:
                ans.append(q)
                dirs[4] = 1
            elif dirs[5] == 0 and q[0] - king[0] < 0 and q[0] - king[0] == q[1] - king[1]:
                ans.append(q)
                dirs[5] = 1
            elif dirs[6] == 0 and q[0] - king[0] < 0 and q[1] - king[1] > 0 and q[0] - king[0] == -(q[1] - king[1]):
                ans.append(q)
                dirs[6] = 1
            elif dirs[7] == 0 and q[0] - king[0] > 0 and q[1] - king[1] < 0 and q[0] - king[0] == -(q[1] - king[1]):
                ans.append(q)
                dirs[7] = 1
            else:
                continue
                
        return ans
                
                