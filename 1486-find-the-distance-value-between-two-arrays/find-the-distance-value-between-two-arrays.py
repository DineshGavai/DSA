class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res=0
        for i in range(len(arr1)):
            flag=True
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j]) <= d:
                    flag=False
                    break
            if flag:
                res+=1
        return res
                