class Solution:
    def countAndSay(self, n: int) -> str:
        if(n == 1):
            return '1'
        
        previous = self.countAndSay(n - 1)
        
        return self.getNextStr(previous)
        
    def getNextStr(self, s):
        if not s:
            return ''
        num = self.getRepeatNum(s)
        
        return str(num) + s[0] + self.getNextStr(s[num:])
    
    def getRepeatNum(self, s):
        count = 1
        letter = s[0]
        for i in s[1:]:
            if i == letter:
                count += 1
            else:
                break
        return count