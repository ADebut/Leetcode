class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        return (max(self.dp(nums[:-1]), self.dp(nums[1:])))
                
    def dp(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0 for x in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            
        return dp[-1]