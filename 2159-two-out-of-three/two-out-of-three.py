class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        temp=[]
        temp.append(list(set(nums1) & set(nums3)))
        temp.append(list(set(nums1) & set(nums2)))
        temp.append(list(set(nums2) & set(nums3)))
        res=set()
        for i in temp:
            for j in i:
                res.add(j)
        return list(res)