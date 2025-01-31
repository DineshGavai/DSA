class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        temp=[]
        for i in grid:
            for j in i:
                temp.append(j)
        print(temp)
        seen=set()
        repeated=0
        missing=0
        for i in range(1,len(temp)+1):
            if temp[i-1]  in seen:
                repeated=temp[i-1]
            else:
                seen.add(temp[i-1])
            
            if i not in temp:
                missing=i
        
        return [repeated,missing]