class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if (len(nums) < 2 or k < 0):
            return 0
        count = 0
        nums.sort()
        right = 0;
        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            

            right = max(right, i + 1)
            while (right < len(nums)):
                if (nums[right] - k == nums[i]):
                    count += 1
                    break
                
                elif (nums[right] - k < nums[i]):
                    right += 1
                else:
                    break
                
        return count