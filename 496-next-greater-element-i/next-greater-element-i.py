class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums1)):
            idx=nums2.index(nums1[i])
            flag=False
            for j in range(idx,len(nums2)):
                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    flag=True
                    break
            if flag==False:
                res.append(-1)  
        return res
            