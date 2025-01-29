class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dummy=dict()
        for i in range(len(names)):
            dummy[heights[i]]=names[i]
        sorted_dict=dict(sorted(dummy.items(),reverse=True))
        return [val for key,val in sorted_dict.items()]