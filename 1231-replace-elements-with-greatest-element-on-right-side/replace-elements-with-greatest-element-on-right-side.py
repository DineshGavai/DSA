class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # res=[]
        max_elem=-1
        for i in range(len(arr)-1,-1,-1):
            new_max=max_elem
            max_elem=max(new_max,arr[i])
            arr[i]=new_max
        return arr
        
        
        
        # for i in range(len(arr)-1):
        #     max_elem=max(arr[i+1:])
        #     res.append(max_elem)
        # res.append(-1)
        # return res