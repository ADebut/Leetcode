class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        ans = len(nums) + 1
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            while(total >= s):
                ans = min(ans, i + 1 - left)
                total -= nums[left]
                left += 1
        if ans != len(nums) + 1:
            return ans
        else:
            return 0