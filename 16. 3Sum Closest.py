class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = []
        nums.sort()
        mi = 2**31 - 1
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    nowMin = abs(nums[i] + nums[left] + nums[right] - target)
                    if nowMin < mi:
                        res = (nums[i], nums[left], nums[right])
                        mi = nowMin
                    left += 1
                elif nums[i] + nums[left] + nums[right] > target:
                    nowMin = abs(nums[i] + nums[left] + nums[right] - target)
                    if nowMin < mi:
                        res = [nums[i], nums[left], nums[right]]
                        mi = nowMin
                    right -= 1
                else:
                    return target
        
        return sum(res)