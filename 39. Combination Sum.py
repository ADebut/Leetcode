class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []
        self.backtrack(ans, temp, candidates, target, 0)
        return ans
    
    def backtrack(self, ans, temp, candidates, remain, nowIndex):
        if remain < 0:
            return
        elif remain == 0:
            ans.append(copy.deepcopy(temp))
        else:
            for i in range(nowIndex, len(candidates)):
                temp.append(candidates[i])
                self.backtrack(ans, temp, candidates, remain - candidates[i], i)
                temp.pop()