class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        total = 0
        dic = collections.defaultdict(int)
        dic[0] = 1
        for i in range(len(nums)):
            total += nums[i]
            if total - k in dic:
                cnt += dic[total - k]
            dic[total] += 1
        return cnt