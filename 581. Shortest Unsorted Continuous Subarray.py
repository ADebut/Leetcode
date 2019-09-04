class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        isStart = False
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start = i
                isStart = True
                break
        for j in range(len(nums) - 1, 0, -1):
            if nums[j] != sorted_nums[j]:
                end = j
                break
        if isStart:
            return end - start + 1
        else:
            return 0