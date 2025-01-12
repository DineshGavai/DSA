class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_w=0
        for i in accounts:
            temp=sum(i)
            max_w=max(max_w,temp)
        return max_w