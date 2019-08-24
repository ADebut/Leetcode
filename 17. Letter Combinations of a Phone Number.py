class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': ['a', 'b', 'c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'], \
              '7': ['p','q','r','s'], '8': ['t','u','v'], '9':['w','x','y','z']}
        res = []
        for i in range(len(digits)):
            if i == 0:
                res = dic[digits[i]]
                continue
            expend = []
            for r in range(len(res)):
                
                for s in dic[digits[i]]:
                    expend.append(res[r] + s)
            res = expend
        return res