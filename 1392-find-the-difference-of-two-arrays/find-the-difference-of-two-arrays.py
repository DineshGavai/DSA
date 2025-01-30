class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1=set()
        ans2=set()
        for i in range(len(nums1)):
            if nums1[i]  not in nums2:
                ans1.add(nums1[i])

        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                ans2.add(nums2[i])

        return [list(ans1),list(ans2)]