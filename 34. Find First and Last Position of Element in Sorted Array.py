class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if nums[i] == target:
                left = i
                break
        else:
            return [-1, -1]
            
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                right = j
                break
        return [i, j]