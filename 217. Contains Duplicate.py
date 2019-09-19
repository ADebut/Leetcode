class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = dict()
        for i in nums:
            if i not in num:
                num[i] = 0
            else:
                return True
        return False