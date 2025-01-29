class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1==nums2:
            return 0
        max1=max(nums1)
        max2=max(nums2)
        diff=max2-max1
        return diff