class Solution:
    def canFindSum(self, nums, target, ind, n, d):
        if target in d: return d[target] 
        if target == 0: d[target] = True
        else:
            d[target] = False
            if target > 0:
                for i in range(ind, n):
                    if self.canFindSum(nums, target - nums[i], i+1, n, d):
                        d[target] = True
                        break
        return d[target]
    def canPartition(self, nums: List[int]) -> bool:
        # total = sum(nums)
        # nums.sort()
        # res = 0
        # for i in range(len(nums)):
        #     res += nums[i]
        #     if total//2 == res:
        #         break
        # if i < len(nums) - 1:
        #     another = sum(nums[i+1:])
        # else:
        #     return False
        # if another == total//2:
        #     return True
        # else:
        #     return False
        # if sum(nums) & 1 == 0:
        #     target = sum(nums) >> 1
        #     cur = {0}
        #     for i in nums:
        #         cur |= {i + x for x in cur}
        #         if target in cur:
        #             return True
        # return False

    
        s = sum(nums)
        if s % 2 != 0: return False
        return self.canFindSum(nums, s/2, 0, len(nums), {})