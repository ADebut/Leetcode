class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        if len(nums1)%2 == 1:
            median = nums1[int((len(nums1)-1)/2)]
        else:
            median = (nums1[int(len(nums1)/2 - 1)] + nums1[int(len(nums1)/2)]) /2
        return median