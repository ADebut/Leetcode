class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) <= 1:
            return len(tasks)
        
        if n == 0:
            return len(tasks)
        
        d = {}
        for t in tasks:
            if t not in d:
                d[t] = 0
            d[t] += 1
            
        maxFreq = max(d.values())
        
        num = maxFreq + n * (maxFreq - 1)
        
        cnt = 0
        for key in d:
            if d[key] == maxFreq:
                cnt += 1
                
        num += (cnt - 1)
        
        if num < len(tasks):
            return len(tasks)
        else:
            return num