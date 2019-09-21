class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        MAX = nums[0]
        dp_min = [0 for x in range(len(nums))]
        dp_max = [0 for x in range(len(nums))]
        dp_min[0] = dp_max[0] = nums[0]
        for i in range(1, len(nums)):
            dp_max[i] = max([dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i], nums[i]])
            dp_min[i] = min([dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i], nums[i]])
            MAX = max(MAX, dp_max[i])
        return MAX