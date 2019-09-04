class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        maxi = nums[0]
        for i in range(len(nums)):
            if dp[i - 1] >= 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
            maxi = max(maxi, dp[i])
        return maxi