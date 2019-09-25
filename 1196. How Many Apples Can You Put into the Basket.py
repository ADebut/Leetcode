class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        units = 5000
        for i in range(len(arr)):
            
            if units >= arr[i]:
                units -= arr[i]
            else:
                i -= 1
                break
        return i + 1
            