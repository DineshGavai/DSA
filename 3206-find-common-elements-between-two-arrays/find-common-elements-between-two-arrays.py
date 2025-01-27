class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        count1=0
        count2=0
        for i in nums1:
            if i in nums2:
                count1+=1
        for i in nums2:
            if i in nums1:
                count2+=1
        
        res.append(count1)
        res.append(count2)
        return res