class Solution:
    def minimumChairs(self, s: str) -> int:
        min_chair=0
        count=0
        for i in s:
            if i =="E":
                count+=1
            else:
                count-=1
            print(count)
            min_chair=max(min_chair,count)
        return min_chair
