class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while (lo <= hi):
            mid = lo + (hi - lo) // 2
            num = nums[mid]
            #nums [ mid ] 和 target 在同一段
            if ((nums[mid] < nums[0]) == (target < nums[0])):
                num = nums[mid]
            #nums [ mid ] 和 target 不在同一段，同时还要考虑下变成 -inf 还是 inf。
            
            else:
                if target < nums[0]:
                    num = -2 ** 31
                else:
                    num = 2 ** 31 - 1
            if (num < target):
                lo = mid + 1
            elif (num > target):
                hi = mid - 1
            else:
                return mid
        
        return -1