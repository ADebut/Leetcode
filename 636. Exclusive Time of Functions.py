class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0] * n
        
        for log in logs:
            idx,tag,time = log.split(":")
            
            if tag == "start":
                stack.append([idx, time])
            elif tag == "end" and idx == stack[-1][0]:
                _, startTime = stack.pop()
                timeTaken = int(time) - int(startTime) + 1
                result[int(idx)] += timeTaken
                print(result)
                if stack:
                    result[int(stack[-1][0])] -= timeTaken
                print(result)
                    
        return result