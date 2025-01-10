class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum=0
        rsum=0
        for i in range(k):
            lsum+=cardPoints[i]
        
        max_sum=lsum
        r_idx=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[r_idx]
            r_idx-=1
            max_sum=max(max_sum,lsum+rsum)
        return max_sum