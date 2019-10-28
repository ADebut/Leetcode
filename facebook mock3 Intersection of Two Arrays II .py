class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = collections.Counter(nums1)
        nums2 = collections.Counter(nums2)
        ans = []
        for i in nums1:
            while nums1[i] > 0 and nums2[i] > 0:
                ans.append(i)
                nums1[i] -= 1
                nums2[i] -= 1
        return ans