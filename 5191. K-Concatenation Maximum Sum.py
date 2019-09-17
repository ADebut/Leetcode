class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if k == 0:
            return 0
        new = []
        for i in range(k):
            new += arr
        def maxSubArray(nums: List[int]) -> int:
            dp = [0 for i in range(len(nums))]
            maxi = nums[0]
            for i in range(len(nums)):
                if dp[i - 1] >= 0:
                    dp[i] = dp[i - 1] + nums[i]
                else:
                    dp[i] = nums[i]
                maxi = max(maxi, dp[i])
            return maxi
        res = maxSubArray(new)
        if res > 0:
            return res
        else:
            return 0