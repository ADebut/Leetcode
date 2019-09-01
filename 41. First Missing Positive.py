class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        
        nums.sort()
        
        if nums[0] > 1 or nums[-1] < 1:
            return 1
        
        mini = 0
        for i in range(len(nums)):
            if nums[i] < 1:
                continue
            elif nums[i] > 0:
                if nums[i] > mini and nums[i] - 1 == mini:
                    mini = nums[i]
                elif nums[i] > mini and nums[i] - 1 != mini:
                    return mini + 1
                
        return nums[i] + 1