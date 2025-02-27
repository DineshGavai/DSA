class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff=float('inf')
        for i in range(len(arr)-1):
            new_diff=arr[i+1]-arr[i]
            min_diff=min(min_diff,abs(new_diff))
        res=[]
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]==min_diff:
                res.append([arr[i-1],arr[i]])

        return res