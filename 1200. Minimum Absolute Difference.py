class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mini = 2 ** 31 - 1
        for i in range(len(arr) - 1):
            if mini > arr[i + 1] - arr[i]:
                mini = arr[i + 1] - arr[i]
        ans = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == mini:
                ans.append([arr[i], arr[i + 1]])
        return ans