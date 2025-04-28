class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq=dict()
        stack=[]
        for i in arr:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for item,count in freq.items():
            if item==count:
                stack.append(item)
        return max(stack) if stack else -1
