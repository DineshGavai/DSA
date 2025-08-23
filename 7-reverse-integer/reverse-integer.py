class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN,INT_MAX=-2**31,2**31-1
        neg= x < 0
        num=str(abs(x))[::-1]
        res=int(num)
        if neg:
            res=-res
        if res < INT_MIN or res >INT_MAX:
            return 0
        return res
