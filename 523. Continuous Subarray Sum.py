class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # if k == 0:
        #     return False
        # i = 0
        # j = 1
        # while(i < len(nums) - 1):
        #     if sum(nums[i: j + 1]) % k == 0:
        #         return True
        #     j += 1
        #     if j == len(nums):
        #         i += 1
        #         j = i + 1
        # return False
        if k==0:
            return any(nums[i]+nums[i+1]==0 for i in range(len(nums)-1))
        m, rem = {0:-1}, 0
        for i in range(len(nums)):
            rem = (rem+nums[i])%k
            if rem in m and i-m[rem]>1:
                return True
            if rem not in m:
                m[rem] = i
        return False